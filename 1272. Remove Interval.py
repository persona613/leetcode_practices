"""
293 ms runtime beats 74.54%
23.34 MB memory beats 93.52%
"""
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        lo = toBeRemoved[0]
        hi = toBeRemoved[1]
        for l, r in intervals:
            if r <= lo or l >= hi:
                res.append([l, r])
            elif l < lo and r > hi:
                res.append([l, lo])
                res.append([hi, r])
            elif l < lo < r:
                res.append([l, lo])
            elif l < hi < r:
                res.append([hi, r])
            else:
                pass
        return res
