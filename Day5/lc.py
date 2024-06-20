l=['ab.cd.ed','gee.lii']
re=[]
for i in l:
    y=[x for x in i.split('.')]
    re.extend(y)
print(re)