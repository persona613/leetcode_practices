"""
Time Limit Exceeded
37 / 38 testcases passed
"""
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sa = sorted(set(arr))
        res = []
        for a in arr:
            res.append(sa.index(a)+1)
        return res


        # sa = sorted(set(arr))
        # rd = {v:i for i, v in enumerate(sa, 1)}
        # res = []
        # for a in arr:
        #     res.append(rd[a])
        # return res