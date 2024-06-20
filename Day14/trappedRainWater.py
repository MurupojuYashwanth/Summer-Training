l=list(map(int,input().split()))  #2,5,2,3,6,7,1,0,5,7
n=len(l)
left=[0]*n
right=[0]*n
left[0]=l[0]
right[n-1]=l[n-1]
for i in range(1,n):
    left[i]=max(l[i],left[i-1])
for i in range(n-2,-1,-1):
    right[i]=max(l[i],right[i+1])
s=0
for i in range(n):
    mi=min(left[i],right[i])
    #print(left[i],right[i])
    s+=(mi-l[i])
print(s)
print(right)
print(left)
