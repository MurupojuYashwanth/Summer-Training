def palin(n,s):
    if not n:
        return s
    s=s*10+(n%10)
    return palin(n//10,s)
n = int(input()) 
t=n
su = palin(n,0)
if su==n:
    print(n)
else:
    sl=len(str(n))
    st=str(n)
    if sl%2==0:
        rem = str(int(st[:(sl//2)])+1)
        print(rem+rem[::-1])
    else:
        rem = str(int(st[:(sl//2+1)])+1)
        s=rem[:-1]
        print(rem+s[::-1])
