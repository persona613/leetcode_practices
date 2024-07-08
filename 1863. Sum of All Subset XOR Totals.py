"""
57 ms runtime beats 51.16%
16.60 MB memory beats 33.82%
"""
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        # idx, path sum
        def backtracking(i, ps):
            nonlocal n
            if i == n:
                return 0
            
            sbsum = 0
            for j in range(i, n):
                ps ^= nums[j]
                sbsum += ps + backtracking(j + 1, ps)
                ps ^= nums[j]
            return sbsum

        n = len(nums)
        return backtracking(0, 0)