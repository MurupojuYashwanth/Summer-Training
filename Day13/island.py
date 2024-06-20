def mat(l,i,j,n):
    x=1
    if i+1<n:
        if l[i+1][j]==1:
            l[i+1][j]=0
            x+=mat(l,i+1,j,n)
    if j+1<n:
        if l[i][j+1]==1:
            l[i][j+1]=0
            x+=mat(l,i,j+1,n)
    if i-1>=0:
        if l[i-1][j]==1:
            l[i-1][j]=0
            x+=mat(l,i-1,j,n)
    if j-1>=0:
        if l[i][j-1]==1:
            l[i][j-1]=0
            x += mat(l,i,j-1,n)
    return x

n=int(input())
l=[]
for i in range(n):
    m=[]
    for j in range(n):
        m.append(int(input()))
    l.append(m)
for i in l:
    print(i)
ma = float('-inf')
co=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            c=mat(l,i,j,n)
            l[i][j]=0
            print(c)
            co+=1
            if c>ma:
                ma=c
print("islands=",co)
print("no of area=",ma-1)

'''

5
0
1
0
0
1
1
0
0
1
1
0
0
0
0
0
1
0
0
0
0
1
0
0
0
1

'''
            