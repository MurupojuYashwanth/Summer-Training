def summ(i, j, sums, el, ol):
    if i == len(el):
        return sums
    if j == len(ol):
        return summ(i + 1, 0, sums, el, ol)
    s = el[i] + ol[j]
    sums.append(s)
    return summ(i, j + 1, sums, el, ol)

def even_odd_sum(l1, l2):
    el = [x for x in l1 if x % 2 == 0]
    ol = [x for x in l2 if x % 2 != 0]
    sums = []
    return summ(0, 0, sums, el, ol)
l1 = list(map(int, input().split()))  # 6,3,2,9,4,7
l2 = list(map(int, input().split()))  # 8,7,5,3,6,9

# Output
print(even_odd_sum(l1, l2))
