class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda i: i[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            last = result[-1][1]

            if start <= last:
                result[-1][1] = max(last, end)
            else:
                result.append([start, end])
        
        return result
        