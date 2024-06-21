s = input()
k = int(input())
k=k%26
st=''
for i in s:
    #x =(ord(i)-k-97)%26+97
    #st+=chr(x)
    x=(ord(i)-k)
    if x<97:
        x+=26
    st+=chr(x)
print(st)