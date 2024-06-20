l=list(map(float,input().split()))
e,o,f=0,0,0
for i in l:
    if i.is_integer():
        if i%2==0:
            e+=i
        else:
            o+=i
    else:
        f+=i
print('f=',f)
print('e=',e)
print('o=',o)






# l=list(map(float,input().split()))
# e,o,f=0,0,0
# for i in l:
#     if ((i*10)%10)==0:
#         if i%2==0:
#             e+=i
#         else:
#             o+=i
#     else:
#         f+=i
# print('f=',f)
# print('e=',e)
# print('o=',o)











# l=list(map(float,input().split()))
# e,o,f=0,0,0
# for i in l:
#     if i%1==0:
#         if i%2==0:
#             e+=i
#         else:
#             o+=i
#     else:
#         f+=i
# print('f=',f)
# print('e=',e)
# print('o=',o)
