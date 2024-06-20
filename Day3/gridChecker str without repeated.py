n = int(input())
l = []
for i in range(n):
    m = []
    for j in range(n):
        m.append(input())
    l.append(m)
print(l)
s = input()
for i in range(len(s)):
    if s[i] not in l[i%n]:
        print(False)
        break
else:
    print(True)
    
    
    

# for idx, char in enumerate(s):
#     if char not in l[idx % n]:
#         print(False)
#         break
# else:
#     print(True)
