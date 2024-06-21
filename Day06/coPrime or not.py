import math
a = int(input())
b = int(input())
x= math.gcd(a,b)
if x==1:
    print("Co-Prime")
else:
    print("Not a Co-Prime")
    
# for i in range(2,min(a,b)+1):
#     if a%i==0 and b%i==0:
#         print("Not a co prime")
#         break
# else:
#     print("Co Prime")