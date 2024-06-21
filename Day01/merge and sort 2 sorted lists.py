 #list1=[2,5,7,9]
 #list2=[1,3,6,7,10,13]
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
l=[]
l1,l2=len(list1),len(list2)
i=0
j=0
while i<l1 and j<l2:
    if list1[i]<list2[j]:
        l.append(list1[i])
        i+=1
    else:
        l.append(list2[j])
        j+=1
l+=list1[i:]+list2[j:]
print(l)