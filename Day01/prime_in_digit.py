# n = int(input())
# def is_pr(n):
#     if n<=1:
#         return False
#     for i in range(2, (n//2)+1):
#         if n%i== 0:
#             return False
#     return True
# while True:
#     if is_pr(n):
#         print(n)
#         break
#     n+=1
    
    
    

n = int(input())   #primes in digit
c=0
def is_pr(n):
    if n<=1:
        return False
    for i in range(2, (n//2)+1):
        if n%i== 0:
            return False
    return True
for i in str(n):
    if is_pr(int(i)):
        c+=1
print(c)



#n=int(input())
# c=0
# while n:
#     if(n%10 in [2,3,5,7]):
#         c+=1
#     n//=10
# print(c)
