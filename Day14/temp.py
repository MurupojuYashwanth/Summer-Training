def paths(n, m):
    # Initialize a dp array with dimensions (n x m)
    dp = [[0] * m for _ in range(n)]

    # Base case: There is exactly one way to be at the bottom-right corner
    dp[n-1][m-1] = 1

    # Fill the dp table from bottom-right corner to top-left corner
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i == n-1 and j == m-1:
                continue  # Skip the bottom-right corner since it's already initialized
            if i + 1 < n:
                dp[i][j] += dp[i+1][j]  # Move down
            if j + 1 < m:
                dp[i][j] += dp[i][j+1]  # Move right
            if i - 1 >= 0:
                dp[i][j] += dp[i-1][j]  # Move up
            if j - 1 >= 0:
                dp[i][j] += dp[i][j-1]  # Move left

    # The result is stored in dp[0][0], which gives the number of paths from (0, 0) to (n-1, m-1)
    return dp[0][0]

# Taking input values for n and m
n = int(input("Enter number of rows (n): "))
m = int(input("Enter number of columns (m): "))

# Calculate and print the number of paths
print(paths(n, m))
