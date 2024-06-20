def fun(coins,amount):
    n=len(coins)
    dp=[float('inf')] * (amount+1)
    print(dp)
    dp[0]=0
    print(dp)
    for coin in coins:
        for j in range(1,amount+1):
            if coin <= j:
                dp[j] = min(dp[j], dp[j-coin] + 1)
    return -1 if dp[amount]==float('inf') else dp[amount]
coins = [1,2,5]
amount = 11
print(fun(coins,amount))