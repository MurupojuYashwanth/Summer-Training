import math

def is_prime(i):
    if i<=1:
        return False
    for j in range(2,(i//2)+1):
        if i%j==0:
            return False
    return True
n1,n2=map(int,input().split())
for i in range(n1,n2):
    if is_prime(i):
        print(i)
    