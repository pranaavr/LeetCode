class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for i in ops:
            if i == '+':
                newSum = record[-1]+record[-2]
                record.append(newSum)
            elif i == 'D':
                record.append(2 * record[-1])
            elif i == 'C':
                record.pop()
            else:
                record.append(int(i))

        print(record)
        return sum(record)