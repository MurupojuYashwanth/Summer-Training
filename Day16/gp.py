class Node:
    def __init__(self):
        self.d = {}
        self.flag = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        t = self.root
        for i in word:
            if i not in t.d:
                t.d[i] = Node()
            t = t.d[i]
        t.flag = True

    def search(self, word):
        t = self.root
        for i in word:
            if i not in t.d:
                return False
            t = t.d[i]
        return t.flag

    def searchPrefix(self, word):
        t = self.root
        for i in word:
            if i not in t.d:
                return False
            t = t.d[i]
        return True

    def wordsWithPrefix(self, prefix):
        t = self.root
        results = []
s
        def find_words(node, prefix):
            if node.flag:
                results.append(prefix)
            for char, child_node in node.d.items():
                find_words(child_node, prefix + char)

        for char in prefix:
            if char not in t.d:
                return []
            t = t.d[char]

        find_words(t, prefix)
        return results
t1 = Trie()
t1.insert('word')
t1.insert('words')
t1.insert('world')
t1.insert('wood')

print(t1.search('wood'))        
print(t1.searchPrefix('woo'))   
print(t1.wordsWithPrefix('wo'))  
