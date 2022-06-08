class Solution:
       
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by first value
        intervals.sort(key = lambda interval : interval[0])
        # return list
        merged = [intervals[0]]
        # merge intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                if intervals[i][1] > merged[-1][1]:
                    merged[-1][1] = intervals[i][1]
            else:
                merged.append(intervals[i])
        
        return merged