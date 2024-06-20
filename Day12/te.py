def max_profit(n, profits):
    intervals = list(zip(n, profits))
    intervals.sort(key=lambda x: x[0][1])
    dp = [0] * len(intervals)
    dp[0] = intervals[0][1]
    for i in range(1, len(intervals)):
        current_profit = intervals[i][1]
        j = i - 1
        while j >= 0 and intervals[j][0][1] > intervals[i][0][0]:
            j -= 1
        if j >= 0:
            current_profit += dp[j]
        print(dp)
        dp[i] = max(dp[i - 1], current_profit)
    
    return dp[-1]
n = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
profits = [5, 6, 5, 4, 11, 2]
print(max_profit(n, profits))  # Output: 17
