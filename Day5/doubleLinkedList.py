class node:
    def __init__(self,u):
        self.data = u
        self.next = None
        self.prev = None
        
class dll:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def addBack(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
#             self.tail.next=node(x)
#             self.tail.next.prev=self.tail
            temp = node(x)
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = self.tail.next
            
    def addFront(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            temp = node(x)
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
            
    def deleteFront(self):
        if self.head==None:
            print(None)
        else:
            self.head=self.head.next
            self.head.prev=None
            
    def deleteBack(self):
        if self.tail==None:
            print(None)
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            
    def linearSearch(self,x):
        if self.head==None:
            print(None)
        else:
            left = self.head
            right= self.tail
            while left.prev!=right:
                if left.data==x or right.data==x:
                    return "Found"
                if left==right:
                    break
                left=left.next
                right=right.prev
            return "NotFound"
        
    def checkLength(self):
        if self.head==None:
            print(None)
        else:
            left = self.head
            right= self.tail
            while left.prev!=right:
                if left==right:
                    return "Odd"
                left = left.next
                right= right.prev       
            return "Even"
        
    def checkPalindrome(self):
        if self.head==None:
            print(None)
        else:
            left = self.head
            right= self.tail
            while left.prev!=right:
                if left.data!=right.data:
                    return "not palindrome"
                if left==right:
                    break
                left = left.next
                right= right.prev       
            return "palindrome"
        
    def printSwapData(self):
        if self.head==None:
            print(None)
        else:
            t = self.head
            t1 = self.tail
            slow = self.head
            fast= self.head
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            t=self.head
            self.head = slow
            self.tail.next = t          
            t.prev = self.tail
            slow.prev.next = None
            self.tail = slow.prev
            slow.prev = None                           
            self.head = slow
            
    def swiftNode(self):
        if self.head==None:
            print(None)
        else:
            f = self.head
            s = f.next
            s.prev = None
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
            self.tail = f
            f.next = None
        
    def checkParanthesis(self):
        l=[]
        c=0
        temp=self.head
        while temp:
            c+=1
            if temp.data in {'{','[','('}:
                l.append(temp.data)
                print(l)
            else:
                if not l:
                    print("empty")
                    break
                if temp.data=='}' and l[-1]=='{':
                    l.pop()
                elif temp.data==')' and l[-1]=='(':
                    l.pop()
                elif temp.data==']' and l[-1]=='[':
                    l.pop()
            temp=temp.next
        print(l)
        if not l:
            print(-1)
        else:
            print(c)
            
    def diffEvenOdd(self):
        
        def check(head,e,o):
            if head==None:
                return (abs(e-o))
            else:
                if head.data%2==0:
                    e+=head.data
                else:
                    o+=head.data
            return check(head.next,e,o)
            
        return check(self.head,0,0)
        
    def countPrimes(self):
        def isPrime(x,i):
            if x <=1:
                return False
            if i>x//2:
                return True
            else:
                if x%i==0:
                    return False
                return isPrime(x,i+1)
        def checkPrime(head,c):
            if head==None:
                return c
            else:
                if isPrime(head.data,2):
                    c+=1
            return checkPrime(head.next,c)
        return checkPrime(self.head,0)
            
    
    def traverseFront(self):
        if self.head==None:
            print(None)
        else:
            temp=self.head
            while temp!=None:
                print(temp.data)
                temp=temp.next
    
    def traverseReverse(self):
        if self.head==None:
            print(None)
        else:
            temp=self.tail
            while temp!=None:
                print(temp.data)
                temp=temp.prev
            
a = dll()
a.addBack(1)
a.addBack(2)
a.addBack(3)
a.addBack(4)
a.addBack(5)
a.addBack(7)
#a.deleteFront()
#a.deleteBack()
a.printSwapData()
# a.swiftNode()
#print(a.diffEvenOdd())
#print(a.countPrimes())
a.traverseFront()
# a.traverseReverse()
#print(a.linearSearch(40))
#print(a.checkLength())
#print(a.checkPalindrome())

# a.addFront('[')
# a.addBack('(')
# a.addBack('{')
# a.addBack('}')
# a.addBack(']')
# a.addBack(']')
# a.traverseFront()
# a.checkParanthesis()
# a.addBack(20)
# a.addBack(20)
