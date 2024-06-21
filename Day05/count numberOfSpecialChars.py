word='LeetCode'
c=0
l=0
if word.isupper():
    c+=1
else:
    l+=1
if c==1 or l==1:
    print(True)
elif ord(word[0])>=65 and ord(word[0])<=90:
    print(True)
else:
    print(False)
