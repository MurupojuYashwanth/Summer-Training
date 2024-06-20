def matrix(l,n,i,j):
    if i+1<n:
        if l[i+1][j]==1:
            l[i+1][j]=2
            matrix(l,n,i+1,j)
    if j+1<n:
        if l[i][j+1]==1:
            l[i][j+1]=2
            matrix(l,n,i,j+1)
    if i-1>=0:
        if l[i-1][j]==1:
            l[i-1][j]=2
            matrix(l,n,i-1,j)
    if j-1>=0:
        if l[i][j-1]==1:
            l[i][j-1]=2
            matrix(l,n,i,j-1)

n=int(input())
l=[]
for i in range(n):
    l1=[]
    for j in range(n):
        l1.append(int(input()))
    l.append(l1)
print(l)

c=0
row = int(input())
col = int(input())
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            c+=1
print(c)
if l[row-1][col-1]==1:
    l[row-1][col-1]=2
    matrix(l,n,row-1,col-1)
    
ub=0
for i in range(n):
    for j in range(n):
        print(l[i][j],end=" ")
    print()
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            ub+=1
print(ub) 