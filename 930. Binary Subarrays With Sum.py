"""
212 ms runtime beats 87.47%
20.36 MB memory beats 45.37%
"""
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = {0: 1}
        curr = ans = 0
        for v in nums:
            curr += v
            pre = curr - goal
            if pre in d:
                ans += d[pre]
            d[curr] = d.get(curr, 0) + 1
        return ans