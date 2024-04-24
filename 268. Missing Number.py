"""
103 ms runtime beats 92.82%
17.82 MB memory beats 64.04%
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
