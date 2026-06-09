class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[intervals[0]]

        for next in intervals[1:]:
            current=res[-1]
            if current[1]>=next[0]:
                current[1]=max(current[1],next[1])
            else:
                res.append(next)
        return res
