row, col = map(int,input().split())
grid = [list(input().split()) for _ in range(row)]
word = input()
n = len(word)
def Traverse(i, j, visited = [], ind = 0):
    if ind >= n:
        return True
    if (not (0<=i<row and 0<=j<col)) or grid[i][j] != word[ind] or (i, j)  in visited:
        return False
    ind += 1
    return Traverse(i + 1, j, visited + [(i, j)], ind) or Traverse(i - 1, j, visited + [(i, j)], ind) or Traverse(i, j + 1, visited + [(i, j)], ind) or Traverse(i, j - 1, visited + [(i, j)], ind)
print()
for i in range(row):
    for j in range(col):
        if Traverse(i, j):
            print(True)
            break
    else:
        continue
    break
else:
    print(False)