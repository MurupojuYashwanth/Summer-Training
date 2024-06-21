n=int(input())
k=1
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n-1:
            print('*',end='')
        else:
            print(k,end='')
            k+=1
    print()
            