def dfs(d,x):
    l.append(x)
    if x==2:
        print(l)
        l.pop()
        return
    for i in d[x]:
        if i not in l:
            dfs(d,i)
    l.pop()
d={5: [7, 3], 7: [5, 4, 3], 4: [7, 8 ,2], 3: [5, 7, 8], 8: [3, 4, 2], 2: [4, 8]}
l=[]
dfs(d,5)
print(l)























'''

Sure, let's analyze the stack for each recursive call in the DFS (Depth-First Search) algorithm:

Initial call: dfs(d, 5)
l is [5]
Recursive call: dfs(d, 7)
l is [5, 7]
Recursive call: dfs(d, 4)
l is [5, 7, 4]
Recursive call: dfs(d, 7) (Note: 7 is already visited, so it won't proceed further)
Recursive call: dfs(d, 8)
l is [5, 7, 4, 8]
Recursive call: dfs(d, 3)
l is [5, 7, 4, 8, 3]
Recursive call: dfs(d, 5) (Note: 5 is already visited, so it won't proceed further)
Recursive call: dfs(d, 7) (Note: 7 is already visited, so it won't proceed further)
Recursive call: dfs(d, 8) (Note: 8 is already visited, so it won't proceed further)
Pop 3
Pop 8
Pop 4
Recursive call: dfs(d, 3) (Note: 3 is already visited, so it won't proceed further)
Pop 7
Recursive call: dfs(d, 3)
l is [5, 3]
Recursive call: dfs(d, 5) (Note: 5 is already visited, so it won't proceed further)
Recursive call: dfs(d, 7) (Note: 7 is already visited, so it won't proceed further)
Recursive call: dfs(d, 8)
l is [5, 3, 8]
Recursive call: dfs(d, 3) (Note: 3 is already visited, so it won't proceed further)
Recursive call: dfs(d, 4) (Note: 4 is already visited, so it won't proceed further)
Recursive call: dfs(d, 2)
l is [5, 3, 8, 2]
Recursive call: dfs(d, 4) (Note: 4 is already visited, so it won't proceed further)
Recursive call: dfs(d, 8) (Note: 8 is already visited, so it won't proceed further)
Pop 2
Pop 8
Pop 3
Pop 5
After all recursive calls, the final value of l is [5].
'''