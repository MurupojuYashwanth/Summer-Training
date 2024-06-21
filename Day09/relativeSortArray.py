from collections import Counter
def relativeSortArray(arr1, arr2):
    count = Counter(arr1)
    result = []
    print(count)
    for num in arr2:
        if num in count:
            result.extend([num] * count[num])
            print(result)
            del count[num]
    remaining = sorted(count.elements())
    result.extend(remaining)

    return result
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(relativeSortArray(arr1, arr2))