class node:
    def __init__(self,u):
        self.data = u
        self.next = None
        self.prev = None
class dll:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def addFront(self,x):
        if self.head == None:
            self.head = node(x)
            self.tail = self.head
        else:
            temp = node(x)
            temp.next = self.head
            self.head = temp
    
    def addBack(self,x):
        if self.head == None:
            self.head = node(x)
            self.tail = self.head
        else:
            temp = node(x)
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = self.tail.next
       
    def deleteFront(self):
        if self.head == None:
            print(None)
        else:
            self.head = self.head.next
            self.head.prev = None
    
    def deleteBack(self):
        if self.head == None:
            print(None)
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    
    def shiftNodes(self):
        if self.head == None:
            print(None)
        else:
            f=self.head
            s=f.next
            s.prev = None           #1 2 3 4     2 1 4 3
            self.head = s
            while f and s:
                t = s.next
                
                s.next = f
                f.prev = s
                
                if t==None or t.next==None:
                    break
                
                f.next = t.next
                t.next.prev = f
                
                f = t
                s = t.next
            self.tail = t
            f.next = None
            
    def countPrime(self):
        temp=self.head
        def isPrime(val,i):
            if val <= 1:
                return False
            if i>val//2:
                return True
            else:
                if val%i==0:
                    return False
            return isPrime(val,i+1)
        def checkPrime(head,c):
            if head==None:
                return c
            else:
                if isPrime(head.data,2):
                    c+=1
            return checkPrime(head.next,c)
        return checkPrime(self.head,0)
    
    def traverse(self):
        if self.head == None:
            print(None)
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp=temp.next
                
    
a = dll()
a.addFront(2)
a.addFront(1)
a.addBack(3)
a.addBack(4)
a.addFront(5)
a.addBack(6)
a.deleteFront()
a.deleteBack()
#a.shiftNodes()
print(a.countPrime())
a.traverse()
                