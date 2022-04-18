class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        missing = 0
        flag = False
        for i in range(min(nums), max(nums)+1):
            if i not in nums:
                missing = i
                flag = True
        if flag == True:
            return missing
        else:
            if 0 not in nums:
                return 0
            else:
                return nums[-1]+1