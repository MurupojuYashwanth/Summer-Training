s = "abcd"
for i in range(len(s)):
    for j in range(i, len(s)):
        print(s[i:j+1])