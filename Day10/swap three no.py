n = list(map(int,input().split(' ')))  # 4 9 8 2 14 3 5 6
for i in range(2,len(n)):
    a = max(n[i],n[i-1],n[i-2])
    b = min(n[i],n[i-1],n[i-2])
    c = n[i]+n[i-1]+n[i-2] -a -b
    n[i] = a
    n[i-1] = c
    n[i-2] = b
print(n)