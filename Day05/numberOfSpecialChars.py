word = "AbBCab"
d={}
sp=0
for i,ch in enumerate(word):
    if ch not in d:
        d[ch]=i
print(d)
for i in d:
    u=chr(ord(i)-32)
    print(u)
    if u in word[d[i]:] and i not in word[d[u]:]:
        sp+=1
print(sp)