def dfs(d,x):
    l.append(x)
    for i in d[x]:
        if i not in l:
            dfs(d,i)
d={5: [7, 3], 7: [5, 4, 3], 4: [7, 8 ,2], 3: [5, 7, 8], 8: [3, 4, 2], 2: [4, 8]}
l=[]
dfs(d,5)
print(l)