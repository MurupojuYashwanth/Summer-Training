def paths(i, j, visited):
    n = len(visited)
    m = len(visited[0])
    if i == n - 1 and j == m - 1:
        return 1
    if i < 0 or j < 0 or i >= n or j >= m or visited[i][j]:
        return 0
    visited[i][j] = True
    total_paths = paths(i + 1, j, visited) + \
                  paths(i - 1, j, visited) + \
                  paths(i, j + 1, visited) + \
                  paths(i, j - 1, visited)
    visited[i][j] = False
    
    return total_paths
n = int(input())
m = int(input())
visited = [[False] * m for _ in range(n)]
print(paths(0, 0, visited))
