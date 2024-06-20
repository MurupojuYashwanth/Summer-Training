# 2
# polikujmnhytbgpvfredvcxswqaz
# abbcdd
#opp: bdca
# 
from collections import Counter
n = int(input())
for i in range(n):
    res=''
    s = input()
    o = input()
    for i in s:
        if i in o:
            res+=(i*o.count(i))
    print(res)

# n = int(input())
# for i in range(n):
#     res=''
#     s = input()
#     o = input()
#     co = Counter(s)
#     print(co)
#     for i in s:
#         if ch in o:
#             res+= i
#     print(res)
    