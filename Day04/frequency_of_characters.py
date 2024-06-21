from collections import Counter
ip = 3, 5, 4, 3, 6, 7, 1, 2, 4, 3, 3, 7, 6, 8, 8
co = Counter(ip)
for num,cnt in co.items():
    print(num,'=',cnt)
    

# l=[]
# for i in ip:
#     if i not in l:
#         l.append(i)
# for i in l:
#     print(i,'=',ip.count(i))
