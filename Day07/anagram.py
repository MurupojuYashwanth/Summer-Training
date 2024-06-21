# s = input()
# k = int(input())
# l = []
# for i in range(k):
#     l1 = []
#     for j in range(k-1):
#         l1.append(input())
#     l.append(l1)
# print(l)
# st=''
# for i in range(len(l)):
#     if l[i][0]=='L':
#         x =l[i][1]
#         a = s[int(x)]
#     else:
#         x =l[i][1]
#         x=int(x)
#         a = s[-x]
#     st+=a
# st = ''.join(sorted(st))
# for i in range(len(s)-2):
#     temp = s[i:i+3]
#     print(temp)
#     temp = ''.join(sorted(temp))
#     if temp==st:
#         print(True)
#         break
# else:
#     print(False)
#     
a=input()
n=int(input())
s=''
for i in range(n):
    b=input()
    if b[0]=='L':
        s=s+a[int(b[1])]
    else:
        s=s+a[-int(b[1])]
s = ''.join(sorted(s))
for i in range(len(s)-2):
    temp = ''.join(sorted(s[i:i+3]))
    if s==temp:
        print(True)
        break
else:
    print(False)