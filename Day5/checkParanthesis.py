s=input()
l=[]
for i in range(len(s)):
    if s[i]=='(' or s[i]=='{' or s[i]=='[':
        l.append(s[i])
    if s[i]=='}' and l[-1]=='{':
        l.pop()
    if s[i]==')' and l[-1]=='(':
        l.pop()
    if s[i]==']' and l[-1]=='[':
        l.pop()
print(i)
if not l:
    print(-1)
else:
    print("not")