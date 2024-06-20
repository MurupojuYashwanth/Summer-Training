# def dfs(d,x):
#     q.append(x)
#     for i in d[x]:
#         if i not in q:
#             dfs(d,i)
# 
# d={5: [7, 3], 7: [5, 4, 3], 4: [7, 8 ,2], 3: [5, 7, 8], 8: [3, 4, 2], 2: [4, 8]}
# q=[]
# dfs(d,5)
# print(q)
def bfs(d,x):
    visited=[]
    q=[x]
    while q:
        f = q.pop(0)
        if f not in visited:
            visited.append(f)
            #print(f,end=" ")
            for i in d[f]:
                if i not in visited:
                    q.append(i)
    print(visited)
d={5: [7, 3], 7: [5, 4, 3], 4: [7, 8 ,2], 3: [5, 7, 8], 8: [3, 4, 2], 2: [4, 8]}
bfs(d,5)