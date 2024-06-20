import math
n=int(input())
def sq(n):
    l,r = 0,int(math.sqrt(n))
    while l<=r:
        if l*l + r*r ==n:
            return True
        elif l*l + r*r >n:
            r-=1
        else:
            l+=1
    return False
print(sq(n))