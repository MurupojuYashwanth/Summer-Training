n = [1,4,3,8,5]
l=[]
for i in range(1,len(n)-1):
    if n[i]>n[i-1] and n[i]>n[i+1]:
        l.append(i)
print(l)














class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
