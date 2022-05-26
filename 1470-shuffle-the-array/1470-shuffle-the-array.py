class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newL = []
        for i in range(n):
            newL.append(nums[i])
            newL.append(nums[i+n])
        return newL
            