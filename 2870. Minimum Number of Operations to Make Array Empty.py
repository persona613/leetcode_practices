"""
585 ms runtime beats 83.64%
31.44 MB memory beats 23.03%
"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = Counter(nums)
        ans = 0
        for v in d.values():
            if v == 1:
                return -1
            elif v % 3 == 0:
                ans += v // 3
            else:
                ans += v // 3 + 1
        return ans