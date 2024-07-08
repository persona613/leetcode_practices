"""
125 ms runtime beats 46.37%
21.15 MB memory beats 21.07%
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        mi = intervals[0][0]
        mx = intervals[0][1]
        res = []
        for st, nd in intervals:
            if st > mx:
                res.append([mi, mx])
                mi = st
                mx = nd
            else:
                mi = min(mi, st)
                mx = max(mx, nd)
        res.append([mi, mx])
        return res