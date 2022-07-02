class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        keys = list(freq.keys())
        vals = list(freq.values())

        res = []

        count = 0
        while count < k:
            index = vals.index(max(vals))
            res.append(keys.pop(index))
            vals.pop(index)
            count+= 1

        return res        