l=list(map(int,input().split()))
t=int(input())
dp=[[0]*(t+1) for _ in range(len(l)+1)]
#print(dp)
for i in range(1,len(l)+1):
    for j in range(1,t+1):
        if l[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            if j == l[i-1]:
                dp[i][j] = 1
            elif dp[i-1][j-l[i-1]]!=0:
                dp[i][j] = dp[i-1][j-l[i-1]]+1
            else:
                dp[i][j] = dp[i-1][j]
print(dp[-1][-1])
print(dp)