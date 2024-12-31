"""
300 ms runtime beats 70.79%
31.45 MB memory beats 10.11%
"""
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        lsum = [0]
        for a in arr:
            lsum.append(a ^ lsum[-1])

        res = []
        for l, r in queries:
            ans = lsum[r + 1] ^ lsum[l]
            res.append(ans)
        return res