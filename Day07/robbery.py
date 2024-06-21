def robber(l):
    if len(l) == 0:
        return 0
    if len(l)==1:
        return l[0]
    y=l[0] + robber(l[2:])
    n=l[1] + robber(l[3:])
    return max(y, n)
    
l=list(map(int,input().split()))
print(robber(l))
#13, 9, 4, 10, 5, 7
