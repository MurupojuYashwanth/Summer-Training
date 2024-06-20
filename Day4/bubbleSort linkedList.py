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
    def bubbleSort(self):
        if(self.head==None):
            print(None)
        temp=self.head
        while(temp.next!=None):
            f=0
            t1=self.head
            p=None
            while(t1.next):
                if t1.data>t1.next.data:
                    f=1
                    t1.data, t1.next.data=t1.next.data,t1.data
                t1=t1.next
            if f==0:
                break    #making t1=p as None
            t1=p   #this is used for n-i (already last ele is sorted) so no need to check it again
            temp=temp.next
    def traverse(self):
        if(self.head==None):
            print(None)
        else:
            temp = self.head
            while(temp!=None):
                print(temp.data)
                temp=temp.next
a = ll()
a.addBack(6)
a.addBack(7)
a.addBack(3)
# a.addFront(5)
a.addBack(8)
a.addBack(4)
a.addBack(2)
a.addBack(0)
a.addBack(1)
# a.deleteAtFront()
# a.deleteAtBack()
# print(a.searchEle(40))
#a.findMid()
#print(a.checkEvenOdd)
a.bubbleSort()
a.traverse()
#6 7 3 8 4 2 0 1