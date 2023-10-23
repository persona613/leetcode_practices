"""
264 ms runtime beats 87.66%
35.6 MB memory beats 52.4%
"""
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sa = sorted(set(arr))
        rd = {v:i for i, v in enumerate(sa, 1)}
        res = []
        for a in arr:
            res.append(rd[a])
        return res