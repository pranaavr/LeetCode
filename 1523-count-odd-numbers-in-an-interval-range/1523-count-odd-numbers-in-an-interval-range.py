import math

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = (high - low) // 2
        if (low%2 == 1 or high%2 == 1):
            n += 1
        return n
        
        