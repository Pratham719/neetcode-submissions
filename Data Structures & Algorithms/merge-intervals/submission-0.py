class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals)
        res=[intervals[0]]

        for cur_start,cur_end in intervals[1:]:
            prev_end=res[-1][1]

            if cur_start<=prev_end:
                res[-1][1]=max(prev_end,cur_end)
            else:
                res.append([cur_start,cur_end])
        return res