class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sumN = 0
        for i in str(n):
            product *= int(i)
            sumN += int(i)
        return product-sumN