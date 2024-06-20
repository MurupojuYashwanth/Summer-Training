# l = list(map(int,input().split()))
# n=len(l)
# for i in range(n-2):
#     for j in range(i+1,n-1):
#         for k in range(j+1,n):
#             print(l[i],l[j],l[k])
def printTriplets(l,k):
    def comb(n,st):
        if len(n)==k:
            print(n)
            return
        for i in range(st,len(l)):
            comb(n+[l[i]],i+1)
        return
    comb([],0)
l = list(map(int,input().split()))
print(printTriplets(l,3))