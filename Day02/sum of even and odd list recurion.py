def oe(a,b,es,os,i):
    if i==len(a):
        return (es,os)
    es+=a[i] if (a[i]&1==0) else 0
    os+=b[i] if (b[i]&1) else 0
    return oe(a,b,es,os,i+1)
    
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(oe(a,b,0,0,0))