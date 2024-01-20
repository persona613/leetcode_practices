"""
251 ms runtime beats 61.59%
20.44 MB memory beats 11.15%
"""
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # counting
        d = defaultdict(int)
        d[0] = 1
        curr = ans = 0
        for v in nums:
            curr += v
            ans += d[curr - goal]
            d[curr] += 1
        return ans