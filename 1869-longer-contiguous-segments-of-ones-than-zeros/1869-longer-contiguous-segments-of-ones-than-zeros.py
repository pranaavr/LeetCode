import re

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = re.findall(r'1+', s)
        zeros = re.findall(r'0+', s)
        if not zeros:
            return True
        elif not ones:
            return False
        if len(max(ones)) > len(max(zeros)):
            return True
        else:
            return False