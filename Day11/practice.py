# def bfs(d,x):
#     visited=[]
#     queue = [x]
#     while queue:
#         val = queue.pop(0)
#         if val not in visited:
#             visited.append(val)
#             for i in d[val]:
#                 if i not in visited:
#                     queue.append(i)
#     return visited
# d={5: [7, 3], 7: [5, 4, 3], 4: [7, 8 ,2], 3: [5, 7, 8], 8: [3, 4, 2], 2: [4, 8]}
# print(bfs(d,5))
# def dfs(d,x):
#     l.append(x)
#     for i in d[x]:
#         if i not in l:
#             dfs(d,i)
#     
# d={5: [7, 3], 7: [5, 4, 3], 4: [7, 8 ,2], 3: [5, 7, 8], 8: [3, 4, 2], 2: [4, 8]}
# l=[]
# dfs(d,5)
# print(l)

# def dfsPrintAllNodes(d,st,end,s):
#     l.append(st)
#     if st == end:
#         print(l,'->',s)
#         l.pop()
#         return
#     for i in d[st]:
#         if i[0] not in l:
#             dfsPrintAllNodes(d,i[0],end,s+i[1])
#     l.pop()
#         
# d = {5: [(7, 4), (3, 2)], 7: [(5, 4), (4, 2), (3, 3)],
#      4: [(7, 2), (8, 4), (2, 1)], 3: [(5, 2), (7, 3), (8, 7)],
#      8: [(3, 7), (4, 4), (2, 2)], 2: [(4, 1), (8, 2)]}
# #d={5: [7, 3], 7: [5, 4, 3], 4: [7, 8 ,2], 3: [5, 7, 8], 8: [3, 4, 2], 2: [4, 8]}
# s=0
# l=[]
# dfsPrintAllNodes(d,5,2,s)


def dfsPrintMinNode(d,st,end,s,m,r):
    l.append(st)
    if st == end:
        #print(l,'->',s)
        if s<m:
            m=s
            r= l.copy()
        l.pop()
        return r, m
    for i in d[st]:
        if i[0] not in l:
            r, m=dfsPrintMinNode(d,i[0],end,s+i[1],m,r)
    l.pop()
    return r, m
        
d = {5: [(7, 4), (3, 2)], 7: [(5, 4), (4, 2), (3, 3)],
     4: [(7, 2), (8, 4), (2, 1)], 3: [(5, 2), (7, 3), (8, 7)],
     8: [(3, 7), (4, 4), (2, 2)], 2: [(4, 1), (8, 2)]}
#d={5: [7, 3], 7: [5, 4, 3], 4: [7, 8 ,2], 3: [5, 7, 8], 8: [3, 4, 2], 2: [4, 8]}
s=0
l=[]
m=10000
print(dfsPrintMinNode(d,5,2,s,m,[]))