def matrix(i,j,k):
    if k==len(s):
        return 1
    if i<0 or j<0 or i>=n or j>=n or l[i][j]!=s[k]:
        return
    if l[i][j]==s[k]:
        l[i][j]=0
    x = matrix(i+1,j,k+1)
    x = matrix(i,j+1,k+1)
    x = matrix(i-1,j,k+1)
    x = matrix(i,j-1,k+1)
    return x

n=int(input())
l=[]
for i in range(n):
    l1=[]
    for j in range(n):
        l1.append(input())
    l.append(l1)
print(l)

c=0
s = input()
for i in range(n):
    for j in range(n):
        if l[i][j]==s[c]:
            c = matrix(i,j,1)
            if c==1:
                print('yes')
                break
else:
    print('no')

    
ub=0
for i in range(n):
    for j in range(n):
        print(l[i][j],end=" ")
    print()
'''

4
t
u
e
d
f
w
o
w
r
o
e
r
d
r
u
i
word
return true if word is present else false
'''
