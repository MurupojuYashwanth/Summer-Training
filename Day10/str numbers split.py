s = input() # hello:5438,car:214,book:8799,apple:2187  oaxp
l = s.split(',')
st=''
x = [i.split(':') for i in l]
print(x)
for i in range(len(x)):
    le = len(x[i][0])
    print(le)
    while le>0:
        if str(le) in (x[i][1]):
            st+=x[i][0][le-1]
            break
        else:
            le-=1
    else:
        st+='x'
print(st)