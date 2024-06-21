def palin(n,s):
    if not n:
        return s
    s=s*10+(n%10)
    return palin(n//10,s)
n=int(input())
v=palin(n,0)
if(v==n):
    print("Palindrome")
else:
    print("Not a Palindrome")