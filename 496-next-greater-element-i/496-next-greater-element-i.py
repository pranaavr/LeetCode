class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for i in nums1:
            answer = -1
            index = nums2.index(i) + 1
            while index < len(nums2):
                if nums2[index] > i:
                    answer = nums2[index]
                    break
                index += 1
            ans.append(answer)
            
        return ans
    