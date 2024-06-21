from collections import Counter
l=list(map(int,input().split()))
# co = Counter(l)
# n=len(l)
# for no,freq in co.items():
#     if freq>n//2:
#         print(no)
        
        
c=1
w=l[0]
for i in range(1,len(l)):
    if l[i]==l[i-1]:
        c+=1
    else:
        if c!=0:
            c-=1
        if c==0:
            w=l[i]
print(w)
        








'''
c = 1
l.sort()
maxx = 1
for i in range(1, len(l)):
    if l[i] == l[i - 1]:
        c += 1
        maxx = max(c, maxx)
    else:
        c = 1
print(maxx) 
'''