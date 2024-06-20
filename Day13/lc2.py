
def countCompleteDayPairs(hours):
    count = 0
    remainder_count = [0] * 24  # Array to store counts of remainders
    print(remainder_count)
    for j in range(len(hours)):
        remainder = hours[j] % 24
        print(remainder)
        count += remainder_count[(24 - remainder) % 24]
        remainder_count[remainder] += 1
    
    return count
l=[12,12,30,24,24]
print(countCompleteDayPairs(l))
