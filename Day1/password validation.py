s=input()
l=len(s)

#ip = asd123!@#   op=1
#ip = 123456789   op=3
#ip = ab          op=6
#ip = A1234B      op=2
d,uc,lc,sp=0,0,0,0
for i in s:
    if(i.islower()):
        lc=1
    elif(i.isupper()):
        uc=1
    elif(ord(i)>47 and ord(i)<58):
        d=1
    else:
        sp=1
v=d+uc+lc+sp
#print(v)
ma=max(8-l,4-v)
if not(ma):
    print(-1)
else:
    print(ma)