class node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
class Bst:
    def __init__(self):
        self.root = None
    def create(self, val):
        if not self.root:
            self.root = node(val)
        else:
            temp = self.root
            while temp:
                previous = temp
                if temp.val > val:
                    temp = temp.left
                elif temp.val < val:
                    temp = temp.right
                else:
                    return 'Data already Exist'
            if previous.val > val:
                previous.left = node(val)
            else:
                previous.right = node(val)
                

    def evenSum(self):
        if not self.root:
            return 'Tree Empty'
        def Traverse(node,s):
            if node:
                if node.val%2==0:
                    s+=node.val + Traverse(node.left,s) + Traverse(node.right,s)
                else:
                    s+=Traverse(node.left,s) + Traverse(node.right,s)
                return s
            return 0
        return Traverse(self.root,0)
        print()
        
    def oddSum(self):
        if not self.root:
            return 'Tree Empty'
        def Traverse(node,o):
            if node:
                if node.val%2==1:
                    o+=node.val + Traverse(node.left,o) + Traverse(node.right,o)
                else:
                    o+=Traverse(node.left,o) + Traverse(node.right,o)
                return o
            return 0
        return Traverse(self.root,0)
        print()
        
    def absDiffEvenOddSum(self):
        if not self.root:
            return 'Tree Empty'
        def Traverse(node,e):
            if node:
                if node.val%2==0:
                    e += node.val + Traverse(node.left,e) + Traverse(node.right,e)
                else:
                    e += -node.val +Traverse(node.left,e) + Traverse(node.right,e)
                return e
            return 0
        return Traverse(self.root,0)
    
    def height(self):   #cls  max(fun(root,l),fun(root,r))+1
        def Traverse(node,c):
            if node:
                h1=Traverse(node.left,c+1)
                h2=Traverse(node.right,c+1)
                return max(h1,h2)
            return c-1
        return Traverse(self.root,0)
    
    def balanced(self):
        def Traverse(node):
            if not node:
                return 0
            height1 = Traverse(node.left)
            if height1 == -1:
                return -1
            height2 = Traverse(node.right)
            if height2 == -1:
                return -1
            if abs(height1 - height2)>1:
                return -1
            return max(height1, height2) + 1
        return Traverse(self.root)!=-1
    
    def countLeafNodes(self):
        def Traverse(node,c):
            if node==None:
                return 0
            if node.left==None and node.right==None:
                return 1
            else:
                return Traverse(node.left,c) + Traverse(node.right,c)
            
        return Traverse(self.root,0)
    
    def sumOfLeafNodes(self):
        def Traverse(node):
            if node==None:
                return 0
            if node.left==None and node.right==None:
                return node.val
            else:
                return Traverse(node.left) + Traverse(node.right)
        return Traverse(self.root)
    
    def search(self,x):
        def Traverse(node,c):
            if node==None:
                return False
            if node.val==x:
                return True
            elif x < node.val:
                return Traverse(node.left,c+1)
            elif x > node.val:
                return Traverse(node.right,c+1)
        return Traverse(self.root,0)
    
    def depth(self,x):
        def Traverse(node,c):
            if node==None:
                return '-inf'
            if node.val==x:
                return c
            elif x < node.val:
                return Traverse(node.left,c+1)
            elif x > node.val:
                return Traverse(node.right,c+1)
        return Traverse(self.root,0)
    
    def inorder(self):
        if not self.root:
            return 'Tree Empty'
        def Traverse(node):
            if node:
                Traverse(node.left)
                print(node.val, end = ' ')
                Traverse(node.right)
        Traverse(self.root)
        print()
    
    def preorder(self):
        if not self.root:
            return 'Tree Empty'
        def Traverse(node):
            if node:
                print(node.val, end = ' ')
                Traverse(node.left)
                Traverse(node.right)
        Traverse(self.root)
        print()
        
    def postorder(self):
        if not self.root:
            return 'Tree Empty'
        def Traverse(node):
            if node:
                Traverse(node.left)
                Traverse(node.right)
                print(node.val, end = ' ')
        Traverse(self.root)
        print()
        
b = Bst()
b.create(3)
b.create(2)
b.create(1)
b.create(5)
b.create(6)
# b.postorder()
s=0
# print(b.evenSum())
# print(b.oddSum())
# print(abs(b.absDiffEvenOddSum()))
# print(b.height())
#print(b.balanced())
print(b.countLeafNodes())
print(b.sumOfLeafNodes())
print(b.search(5))