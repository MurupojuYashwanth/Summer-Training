'''
class Node:
    def __init__(self):
        self.d = {}
        self.flag = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        t = self.root
        for char in word:
            if char not in t.d:
                t.d[char] = Node()
            t = t.d[char]
        t.flag = 1

    def search(self, word):
        t = self.root
        for char in word:
            if char not in t.d:
                return False
            t = t.d[char]
        return t.flag == 1

    def searchPrefix(self, word):
        t = self.root
        for char in word:
            if char not in t.d:
                return False
            t = t.d[char]
        return True

    def maxlengthPrefix(self, words):
        def pairs(node, word):
            nonlocal max_prefix
            if node.flag == 1:
                if len(word) > len(max_prefix):
                    max_prefix = word
                res.append(word)
            for ch, cnode in node.d.items():
                pairs(cnode, word + ch)

        results = []
        for prefix in words:
            t = self.root
            max_prefix = ''
            for char in prefix:
                if char not in t.d:
                    break
                t = t.d[char]
                max_prefix += char
                if t.flag == 1:
                    break  # Stop early if we find a complete word
            res = []
            pairs(t, max_prefix)
            results.append(max(res, key=len) if res else '')  # Find the longest prefix word

        return results

# Example usage:
t1 = Trie()
t1.insert('word')
t1.insert('words')
t1.insert('worlds')
t1.insert('wood')
t1.insert('ant')
t1.insert('apple')
t1.insert('aero')

print(t1.maxlengthPrefix(['w', 'a']))  # Output: ['worlds', 'apple']


'''
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
        
    def maxlengthPrefix(self,words):
        t=self.root
        res=[]
        def pairs(node,word):
            #nonlocal s
            if node.flag==1:
#                 if len(word)>len(s):
#                     s=word
                maxx.append(word)
            for ch in node.d:
                pairs(node.d[ch],word+ch)
        for word in words:
            t=self.root
            #s=''
            maxx=[]
            for i in word:
                if i not in t.d:
                    break
                t=t.d[i]
                #s+=i
#                 if t.flag==1:
#                     break
            #maxx=[]
            pairs(t,i)
            print(maxx)
            res.append(max(maxx, key=len))
        return res
            
                
t1 = Trie()
t1.insert('word')
t1.insert('words')
t1.insert('worlds')
t1.insert('wood')
t1.insert('ant')
t1.insert('apple')
t1.insert('aero')
#print(t1.search('wood'))
#print(t1.searchPrefix('woo'))
print(t1.maxlengthPrefix(['w','a'])) 

