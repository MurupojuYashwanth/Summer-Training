def profit(l):
    m=0
    minn=float('inf')
    for i in range(len(l)):
        if minn<l[i]:
            pr=l[i]-minn
            m=max(m,pr)
        else:
            minn=l[i]
    return m
l=list(map(int,input().split()))
print(profit(l))
#15 3 2 7 8 4   = 6
#5 3 2 7 8 4    = 6
#5 4 2 9 7 1    = 7
#9 8 7 6 5 4    = 0
