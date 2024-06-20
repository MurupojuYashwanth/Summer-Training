n=int(input())
m=int(input())
def paths(i,j,n,m):
    if i==n-1 and j==m-1:
        return 1
    elif i>=n or j>=m:
        return 0
    p1=paths(i+1,j,n,m)
    p2=paths(i,j+1,n,m)
    return p1+p2
print(paths(0,0,n,m))