def dfs(d, x, s):
    l.append(x)
    if x == 2:
        print(l, "=", s)
        l.pop()
        return
    for i in d[x]:
        if i[0] not in l:
            dfs(d, i[0], s + i[1])  
    l.pop()
d = {5: [(7, 4), (3, 2)], 7: [(5, 4), (4, 2), (3, 3)],
     4: [(7, 2), (8, 4), (2, 1)], 3: [(5, 2), (7, 3), (8, 7)],
     8: [(3, 7), (4, 4), (2, 2)], 2: [(4, 1), (8, 2)]}
l = []
s = 0
dfs(d, 5, s)
print(l)
