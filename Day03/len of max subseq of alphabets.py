s=input()
maxx=1
c=1
for i in range(1,len(s)):
    if ord(s[i])==ord(s[i-1])+1:
        c+=1
    else:
        maxx=max(maxx,c)
        c=1
maxx=max(maxx,c)
print(maxx)