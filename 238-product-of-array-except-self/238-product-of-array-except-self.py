import numpy

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        ans.append(numpy.prod(nums[1:]))

        for i in range(1,len(nums)):
            if nums[i] == 0:
                arr = nums[:i]+nums[i+1:]
                res = numpy.prod(arr)
            else:
                q = ans[-1]/nums[i]
                res = q * nums[i-1]
            ans.append(int(res))

        return ans