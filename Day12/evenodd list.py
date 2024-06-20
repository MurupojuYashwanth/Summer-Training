def summ(i, j, l, el, ol):
    if i == len(el):
        return l
    if j == len(ol):
        return summ(i + 1, 0, l, el, ol)
    s = el[i] + ol[j]
    l.append(s)
    return summ(i, j + 1, l, el, ol)

def even(l1, l2, n, i, el, ol):
    if i == n:
        return el, ol
    if l1[i] % 2 == 0:
        el.append(l1[i])
    if l2[i] % 2 != 0:
        ol.append(l2[i])
    return even(l1, l2, n, i + 1, el, ol)
l1 = list(map(int, input().split()))  # 6,3,2,9,4,7
l2 = list(map(int, input().split()))  # 8,7,5,3,6,9
n = len(l1)
el, ol = even(l1, l2, n, 0, [], [])
result = summ(0, 0, [], el, ol)
print(result)
#op [13,11,9,15,9,7,5,11,11,9,7,13]