n=int(input())
k=int(input())
l=[]
for i in range(1,n+1//2):
    if n%i==0:
        l.append(i)
l.append(n)
print(l[-k])