# n = list(map(int,input().split()))
# l=[[n[0]]]
# k=0
# l1=[]
# for i in range(1,len(n)):
#     if n[i] not in l[-1]:
#         l[-1].append(n[i])
#     else:
#         l1.append(n[i])
#         if n[i] not in l1:
#             
#         l.extend(l1)
# print(l)
#op = [[1,2,3,4],[1,2,3],[1,2]]

n = list(map(int, input().split()))
d = {}
for i in range(len(n)):
    if n[i] not in d:
        d[n[i]] = 1
    else:
        d[n[i]] += 1
print(d)














# n = list(map(int, input().split()))
# l = [[n[0]]]
# 
# for i in range(1, len(n)):
#     if n[i] not in l[-1]:
#         l[-1].append(n[i])
#     else:
#         l.append([n[i]])
# 
# print(l)
