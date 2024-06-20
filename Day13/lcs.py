s1 = input()  # aabdc # badc
s2 = input()  
m = len(s1)
n = len(s2)
s=[]
mat = [[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if s1[i-1]==s2[j-1]:
            mat[i][j]=mat[i-1][j-1]+1
        else:
            mat[i][j] = max(mat[i-1][j],mat[i][j-1])
print(mat[-1][-1])             #ex  abcd  axbd
for i in mat:
    print(i)
i=m
j=n
while i>0 and j>0:
    if s1[i-1]==s2[j-1]:
        s+=s1[i-1]
        i-=1
        j-=1
    elif mat[i-1][j]>=mat[i][j-1]:
        i-=1
    else:
        j-=1
print(''.join(s[::-1]))