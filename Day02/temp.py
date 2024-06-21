s="is2 sentence4 This1 a3"
s=s.split()
print(s)
l=[]
y=[]
#print(len(l))
for i in s:
    x=i[-1]
    y.append(i[:-1])
    
    #i.remove(x)
    l.append(x)
print(l)
print(y)
e=[i for _,i in sorted(zip(l,y))]
print(e)





'''

s = "is2 sentence4 This1 a3"
s = s.split()

# Separate words and numbers
words = []
numbers = []
for word in s:
    num = int(''.join(filter(str.isdigit, word)))
    words.append(''.join(filter(str.isalpha, word)))
    numbers.append(num)

# Sort based on numbers
sorted_words = [word for _, word in sorted(zip(numbers, words))]

print(sorted_words)


'''