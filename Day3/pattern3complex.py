n=int(input())
z=1
for i in range(1,(2*n)):
    for j in range(1,(2*n)):
        print((min(i,j,(2*n)-i,(2*n)-j)),end='')
    print()
'''
1111111
1222221
1233321
1234321
1233321
1222221
1111111
'''