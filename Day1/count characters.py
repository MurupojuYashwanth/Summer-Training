ip= 'aaabbaaaddd'
i=1
t=1
while i<len(ip):
    if ip[i] == ip[i-1]:
        t+=1
    else:
        print(ip[i-1]+str(t))
        t=1
    i+=1
print(ip[i-1]+str(t))























# ip= 'aaabbaaaddd'
# i=0
# t=1
# while i<len(ip)-1:
#     if ip[i] == ip[i+1]:
#         t+=1
#     else:
#         print(ip[i]+str(t))
#         t=1
#     i+=1
# print(ip[i]+str(t))

