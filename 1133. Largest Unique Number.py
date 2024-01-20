"""
53 ms runtime beats 53.88%
16.57 MB memory beats 29.85%
"""
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        d = dict()
        for v in nums:
            d[v] = d.get(v, 0) + 1
        res = {k for k in d if d[k]==1}
        return max(res) if res else -1