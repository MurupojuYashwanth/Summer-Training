def summ(l,s,i,t):
    if i==len(l):
        if len(s)==0:
            return 0
        else:
            x=sum(s)
            if x==t:
                return True
            else:
                return False
    if (summ(l,s+[l[i]],i+1,t)):
        return True
    if summ(l,s,i+1,t):
        return True
    return False
l=list(map(int,input().split())) # l= 2 3 5 6 
t=int(input())
print(summ(l,[],0,t))

