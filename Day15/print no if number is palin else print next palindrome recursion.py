def palin(n,s):
    if not n:
        return s
    s=s*10+(n%10)
    return palin(n//10,s)
n = int(input()) 
t=n
while True:
    su = palin(n,0)
    if su==n:
        print(n)
        break
    else:
        n+=1
        t=n

