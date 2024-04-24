"""
46 ms runtime beats 41.26%
16.50 MB memory beats 83.74%
"""
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f = defaultdict(int)
        for v in nums:
            f[v] += 1
        mx = max(f.values())
        cnt = 0
        for k in f:
            if f[k] == mx:
                cnt += 1
        return cnt * mx