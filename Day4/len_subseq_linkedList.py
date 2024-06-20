class node:
    def __init__(self,u):
        self.data = u
        self.next = None
class ll:
    def __init__(self):
        self.head=None
    def addBack(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
    def addFront(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp = node(x)
            temp.next = self.head
            self.head = temp
    def deleteAtFront(self):
        if(self.head==None):
            print(None)
        else:
            self.head = self.head.next #head=head.next
    def deleteAtBack(self):
        if(self.head==None):
            print(None)
        elif(self.head.next==None):
            self.head=None
        else:
            temp=self.head
            while(temp.next.next!=None):
                temp=temp.next
            temp.next=None
    def searchEle(self,x):
        if(self.head==None):
            print(None)
        else:
            temp=self.head
            while(temp.next!=None):
                if temp.data==x:
                    return "Found"
                    break
                temp=temp.next
            return "not Found"
    def findMid(self):
        if(self.head==None):
            print(None)
        else:
            slow=self.head
            fast=self.head
            while fast!=None and fast.next!=None:
                slow=slow.next
                fast=fast.next.next
            print(slow.data)
    def checkEvenOdd(self):
        slow=self.head
        fast=self.head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        if fast==None:
            return 'Even'
        else:
            return 'Odd'
    def traverse(self):
        m=1
        c=0
        if(self.head==None):
            print(None)
        else:
            temp = self.head
            while(temp.next!=None):
                if((temp.data)+1==(temp.next.data)):
                    m+=1
                    maxx=max(c,m)
                    c=maxx
                else:
                    m=1
                temp=temp.next
            print(maxx)
a = ll()
a.addBack(1)
a.addBack(2)
a.addBack(3)
a.addBack(4)
a.addBack(7)
a.addBack(8)
a.addBack(9)
a.addBack(3)
a.addBack(4)
a.addBack(5)
a.addBack(6)
a.addBack(7)
# a.addFront(5)
# 
# a.addBack(40)
# a.addBack(50)
# a.deleteAtFront()
# a.deleteAtBack()
# print(a.searchEle(40))
# a.findMid()
#print(a.checkEvenOdd)
a.traverse()

