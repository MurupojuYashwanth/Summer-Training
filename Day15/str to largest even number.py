s1=input() # tu5g2k1h8  # g5g8gd6h3
s2=input()
l=set()
for i in s1:
    if i.isdigit():
        if i not in l:
            l.add(int(i))
for i in s2:
    if i.isdigit():
        if i not in l:
            l.add(int(i))
l=list(l)
o=l.copy()
l=l[::-1]
if l[-1]%2==0:
    print(*l,sep="")
else:
    for i in range(len(o)):
        if o[i]%2==0:
            p=o[i]
            o.pop(i)
            break
    o.insert(0,p)
    o=o[::-1]
    print(*o,sep="")
# print(x)
