class node:
    def __init__(self, u):
        self.val = u
        self.left = None
        self.right = None

class bst:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = node(val)
        else:
            temp = self.root
            while temp:
                pr = temp
                if temp.val > val:
                    temp = temp.left
                elif temp.val < val:
                    temp = temp.right
                else:
                    return 'Data Exist'
            if val < pr.val:
                pr.left = node(val)
            else:
                pr.right = node(val)

    def preorder(self):
        if not self.root:
            return 'Empty'
        def Traverse(node):
            if node:
                print(node.val, end=" ")
                Traverse(node.left)
                Traverse(node.right)
        Traverse(self.root)
        print()
        
    def inorder(self):
        if not self.root:
            return 'Empty'
        def Traverse(node):
            if node:
                Traverse(node.left)
                print(node.val,end=" ")
                Traverse(node.right)
        Traverse(self.root)
        print()
        
    def postorder(self):
        if not self.root:
            return 'Empty'
        def Traverse(node):
            if node:
                Traverse(node.left)
                Traverse(node.right)
                print(node.val, end=" ")
        Traverse(self.root)
        print()
             
    def evenSum(self):
        def Traverse(node,s):
            if node:
                if node.val%2==0:
                    s += node.val + Traverse(node.left,s) + Traverse(node.right,s)
                else:
                    s += Traverse(node.left,s) + Traverse(node.right,s)
                return s
            return 0
        return Traverse(self.root,0)
    
    def oddSum(self):
        def Traverse(node,o):
            if node:
                if node.val%2!=0:
                    o += node.val + Traverse(node.left,o) + Traverse(node.right,o)
                else:
                    o += Traverse(node.left,o) + Traverse(node.right,o)
                return o
            return 0
        return Traverse(self.root,0)
    
    def absDiff(self):
        def Traverse(node,s):
            if node:
                if node.val%2==0:
                    s += node.val + Traverse(node.left,s) + Traverse(node.right,s)
                else:
                    s += -node.val + Traverse(node.left,s) + Traverse(node.right,s)
                return s
            return 0
        return Traverse(self.root,0)
    
    def height(self):
        if not self.root:
            return 'Empty'
        def Traverse(node,c):
            if node:
                h1 = Traverse(node.left,c+1)
                h2 = Traverse(node.right,c+1)
                return max(h1,h2)
            return c-1
        return Traverse(self.root,0)
    
    def balanced(self):
        def Traverse(node):
            if node==None:
                return 0
            h1 = Traverse(node.left)
            if h1==-1:
                return -1
            h2 = Traverse(node.right)
            if h2 == -1:
                return -1
            if abs(h1-h2)>1:
                return -1
            return max(h1,h2)+1
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
    
    def sumLeafNodes(self):
        def Traverse(node):
            if node==None:
                return 0
            if node.right==None and node.left==None:
                return node.val
            else:
                return Traverse(node.left) + Traverse(node.right)
        return Traverse(self.root)
    
    def search(self,x):
        def Traverse(node):
            if node==None:
                return False
            if node.val == x:
                return True
            if x < node.val:
                return Traverse(node.left)
            elif x > node.val:
                return Traverse(node.right)
            return False
        return Traverse(self.root)
    
    def depth(self,x):
        def Traverse(node,c):
            if node == None:
                return 0
            if node.val == x:
                return c
            elif x < node.val:
                return Traverse(node.left,c+1)
            elif x > node.val:
                return Traverse(node.right,c+1)
            return 
        return Traverse(self.root,0)
    
    def leftView(self):
        if not self.root:
            return 'Empty'
        def Traverse(node,c,l):
            if node==None:
                return
            if c not in l:
                print(node.val,end=" ")
                l.append(c)
            Traverse(node.left,c+1,l)
            Traverse(node.right,c+1,l)
        Traverse(self.root,0,[])
        print()
        
    def rightView(self):
        if not self.root:
            return 'Empty'
        def Traverse(node,c,l):
            if node==None:
                return
            if c not in l:
                print(node.val,end=" ")
                l.append(c)
            Traverse(node.right,c+1,l)
            Traverse(node.left,c+1,l)
        Traverse(self.root,0,[])
        print()
        
#     def topView(self):
#         if not self.root:
#             return 'Empty'
#         def right(node,c,d):
#             if node:
#                 right(node.right,c+1,d)
#                 print(node.val, end=" ")
#         def left(node,c,d):
#             if node:
#                 print(node.val, end=" ")
#                 left(node.left,c-1,d)
#         def Traverse(node,c,d):
#             if node==None:
#                 return
#             if c not in d:
#                 d[c] = node.val
#                 print(node.val,end=" ")
#             left(node.left,c-1,d)
#             right(node.right,c+1,d)
#         Traverse(self.root,0,{})
#         print( )
    def topView(self):
        top_view_list = []
        level_list = []
        def view(Node = self.root):
            node_list = [(self.root,0)]
            i = 0
            while i<len(node_list):
                Node, level = node_list[i]
                if not Node:
                    i += 1
                    continue
                if level not in level_list:
                    top_view_list.append(Node.val)
                    level_list.append(level)
                node_list += [(Node.left, level - 1), (Node.right, level + 1)]
                i += 1
        view()
        return top_view_list
    
    def bottomView(self):
        bottom_view_list = {}
        level_list = []
        def view(Node = self.root):
            node_list = [(self.root,0)]
            i=0
            while i<len(node_list):
                Node,level = node_list[i]
                if not Node:
                    i+=1
                    continue
                bottom_view_list[level] = Node.val
                print(bottom_view_list)
                node_list += [(Node.left,level-1), (Node.right,level+1)]
                i+=1
        view()
        return sorted(bottom_view_list.values())


b = bst()
# b.create(10)
# b.create(5)
# b.create(2)
# b.create(7)
# b.create(3)
# b.create(15)
# b.create(11)
# b.create(20)
# b.create(21)
# b.create(22)
b.create(10)
b.create(5)
b.create(2)
b.create(7)
b.create(4)
b.create(3)
b.create(15)
b.create(11)
b.create(12)
b.create(13)
b.create(14)
b.create(20)
# b.preorder()
#b.inorder()
# b.leftView()
# b.rightView()
#print(b.topView())
# b.topView()
print(b.bottomView())
# b.postorder()
# print(b.evenSum())
# print(b.oddSum())
# print(abs(b.absDiff()))
# print(b.height())
# print(b.countLeafNodes())
# print(b.sumLeafNodes())
# print(b.search(5))
# print(b.depth(5))
