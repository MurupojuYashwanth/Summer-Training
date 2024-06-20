l=list(map(int,input().split()))  # 1 3 4 5  #coin target-17  #op = 4
le=len(l)
n=int(input())
coins=list(range(n+1))
mat=[-1]*(n+1)
mat[0]=0
for i in l:
    for j in range(1,n+1):  #3 4 5 n=7
        if j>=i:
            if mat[j-i]!=-1:
                if mat[j]!=-1:
                    mat[j]=min(mat[j],mat[j-i]+1)
                else:
                    mat[j]=mat[j-i]+1
print(mat[-1])
        
