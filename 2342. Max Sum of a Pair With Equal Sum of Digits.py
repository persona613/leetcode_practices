"""
809 ms runtime beats 70.77%
31.88 MB memory beats 15.59%
"""
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def dsum(num):
            ds = 0
            while num:
                ds += num % 10
                num //= 10
            return ds
        d = dict()
        ans = -1
        for v in nums:
            ds = dsum(v)
            if ds in d:
                ans = max(ans, v + d[ds])
                d[ds] = max(d[ds], v)
            else:
                d[ds] = v
        return ans
