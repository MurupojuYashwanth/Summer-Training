from collections import Counter
x=input()
n=x.upper()
co=Counter(n)
if co['M']==co['F']:
    print(0)
elif co['M']>co['F']:
    print('M')
else:
    print('F')