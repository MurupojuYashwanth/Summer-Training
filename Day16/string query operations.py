class Str:
    def __init__(self):
        self.word = set()
    def ins(self, wo):
        self.word.add(wo)
    def search(self, wo):
        return wo in self.word
    def prefix(self, wo):
        l=len(wo)
        for i in self.word:
            if i[:l]==wo:
                return True
        return False
    def dele(self, wo):
        self.word.remove(wo)
        return self.word
o=Str()
n=int(input())
for i in range(n):
    x=input().split(' ')
    if x[0]=='1':
        o.ins(x[1])
    if x[0]=='2':
        print(o.search(x[1]))
    if x[0]=='3':
        print(o.prefix(x[1]))
    if x[0]=='4':
        print(o.dele(x[1]))
        
        
'''

8
1 school
1 world
1 word
1 scholar
2 word
2 wood
3 sch
4 school


'''
