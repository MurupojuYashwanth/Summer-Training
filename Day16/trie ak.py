class Node:
    def __init__(self):
        self.d = {}
        self.flag = False

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        t = self.root
        i = 0
        while i < len(word) and word[i] in t.d:
            t = t.d[word[i]]
            i += 1
        while i < len(word):
            t.d[word[i]] = Node()
            t = t.d[word[i]]
            i += 1
        t.flag = True

# Example usage:
t1 = Trie()
t1.insert('word')
