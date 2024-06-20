class Node:
    def __init__(self):
        self.d ={}
        self.flag=0
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self,word):
        t=self.root
        for i in word:
            if i not in t.d:
                t.d[i]=Node()
            t=t.d[i]
        t.flag=1
                
    def search(self,word):
        t=self.root
        for i in word:
            if i not in t.d:
                return False
            t=t.d[i]
        if t.flag==1:
            return True
        else:
            return False
        
    def searchPrefix(self,word):
        t=self.root
        for i in word:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
        
    def wordsWithPrefix(self,word):
        t=self.root
        res=[]
        def pairs(node,word):
            if node.flag==1:
                res.append(word)
            for ch in node.d:
                pairs(node.d[ch],word+ch)
        for i in word:
            if i not in t.d:
                return False
            t=t.d[i]
        pairs(t,word)
        return res
    
    def maxlengthPrefix(self,words):
        res=[]
        def pairs(node,word):
            if node.flag==1:
                maxx.append(word)
            for ch in node.d:
                pairs(node.d[ch],word+ch)
        for word in words:
            t=self.root
            maxx=[]
            for i in word:
                if i not in t.d:
                    break
                t=t.d[i]
            pairs(t,i)
            print(maxx)
            res.append(max(maxx, key=len))
        return res
            
                
t1 = Trie()
t1.insert('word')
t1.insert('words')
t1.insert('world')
t1.insert('wood')
#print(t1.search('wood'))
#print(t1.searchPrefix('woo'))
# print(t1.maxlengthPrefix(['w','a']))
print(t1.wordsWithPrefix('w'))