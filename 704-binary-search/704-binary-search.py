class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            half = left + (right-left) // 2
            if nums[half] == target:
                return half
            elif target < nums[half]:
                right = half - 1
            else:
                left = half + 1
        return -1
            
        
        