ip='placements'
a=''
for i in ip:
    if(i.islower()):
        if i in 'aeiou':
            a+=i.upper()
        else:
            a+=i
    if(i.isupper()):
        if i in 'AEIOU':
            a+=i.upper()
print(a)
        