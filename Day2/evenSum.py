def oe(n,es):
    if n==1:
        return es
    es+=n if (n&1==0) else 0
    return oe(n-1,es)
    
n=int(input())
print(oe(n,0))


# def oe(n):
#     if n==0:
#         return 0
#     return n+oe(n-2)
# n=int(input())
# if(n%2==0):
#     print(oe(n))
# else:
#     print(oe(n-1,0))