"""
71 ms runtime beats 61.79%
16.80 MB memory beats 36.81%
"""
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = []
        d = defaultdict(int)
        for arr in nums:
            for a in arr:
                d[a] += 1
        n = len(nums)
        for k in d:
            if d[k] == n:
                res.append(k)
        return sorted(res)