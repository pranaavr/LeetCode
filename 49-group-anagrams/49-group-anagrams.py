import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alph = string.ascii_lowercase
        counts = []

        for s in strs:
            count = [0]*26
            for l in s:
                index = alph.index(l)
                count[index] += 1
            counts.append(count)

        hash = {}

        for i in range(len(counts)):
            val = str(counts[i])
            if val in hash:
                hash[val].append(i)
            else:
                hash[val] = [i]

        groups = list(hash.values())

        res = []

        for g in groups:
            group = []
            for num in g:
                group.append(strs[num])
            res.append(group)

        return res