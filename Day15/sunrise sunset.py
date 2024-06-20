l=list(map(int,input().split())) #3 5 9 6 8 10
le=0
ri=len(l)-1
n=len(l)
c=1
ma=l[0]
for i in range(1,len(l)):
    if l[i]>ma:
        #print(c,l[i],ma)
        c+=1
        ma=l[i]
mi=l[-1]
c1=1
for i in range(n-2,-1,-1):
    if l[i]>ma:
        print(c,l[i],ma)
        c1+=1
        mi=l[i]
print(c,c1)