def summ(n):
    s=0
    while n:
        r=n%10
        s+=r
        n//=10
    return s
n = int(input())  #list(map(int,n))
t=n
while True:
    while n>9: 
        su = summ(n)
        n=su
    if n in [2,3,5,7]:
        print(t)
        break
    else:
        t+=1
        n=t