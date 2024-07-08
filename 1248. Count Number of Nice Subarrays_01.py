"""
666 ms runtime beats 82.92%
25.20 MB memory beats 30.59%
"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # pre-sum on fly
        curr = ans = 0
        d = {0: 1}
        for v in nums:
            curr += v % 2
            if curr - k in d:
                ans += d[curr - k]
            d[curr] = d.get(curr, 0) + 1
        return ans