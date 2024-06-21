n=int(input())
for i in range(n):
    for j in range(n-i):
        print('-',end='')
    for k in range(i+1):
        print(chr(97+k),end='')
    for m in range(i):
        print(chr(97+m),end='')
    for l in range(n-i):
        print('-',end='')
    print()
