n = int(input())
l = []
for i in range(n):
    l.append(list(input()))
print(l)
s = input()
for i in range(len(s)):
    if s[i] not in l[i%n]:
        print(False)
        break
    l[i%n].remove(s[i])
else:
    print(True)