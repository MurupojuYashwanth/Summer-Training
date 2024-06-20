# d={5: [7, 3], 7: [5, 4, 3], 4: [7, 8 ,2], 3: [5, 7, 8], 8: [3, 4, 2], 2: [4, 8]}
d = {5: [(7, 4), (3, 2)], 7: [(5, 4), (4, 2), (3, 3)],
     4: [(7, 2), (8, 4), (2, 1)], 3: [(5, 2), (7, 3), (8, 7)],
     8: [(3, 7), (4, 4), (2, 2)], 2: [(4, 1), (8, 2)]}
st=5
end=2
q = [(st,[],0)]
res=[]
i=0
m=99999
while i<len(q):
    node,path,c = q[i]
    if node==end:
        if c<m:
            m=c
            r = path+[node]
        res.append((path+[node],c))
        i+=1
        continue
    for j in d[node]:
        if j[0] not in path:
            q.append((j[0],path+[node],c+j[1]))
    i+=1
print(res)
print("min path = ",r,"\nCost=",m)
