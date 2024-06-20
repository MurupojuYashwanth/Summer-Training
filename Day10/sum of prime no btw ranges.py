def isPrime(no):
    if no<=1:
        return False
    for x in range(2,(no//2)+1):
        if no%x==0:
            return False
    return True
l=list(map(int,input().split()))
res=[]
s=0
i=1
j=0
while i<len(l):
    for k in range(l[i],l[j],-1):
        if isPrime(k):
            res.append(k)
            s+=k
            break
        
    i+=1
    j+=1
print(res)
print(s)