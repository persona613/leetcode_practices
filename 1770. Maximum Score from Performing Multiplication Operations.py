"""
1038 ms runtime beats 36.04%
152.64 MB memory beats 24.12%
"""
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # op for multiplers, j for nums
        @cache
        def dp(op, j):
            if op == m:
                return 0
            # not take curr-j: p[op] * n[R] (right side)
            # right_size = taken from right = opreations - j(taken form left)
            right_size = op - j 
            curr_right = (n - 1) - right_size
            case1 = dp(op + 1, j) + multipliers[op] * nums[curr_right]
            # take curr-j: p[op] * n[j]
            case2 = dp(op + 1, j + 1) + multipliers[op] * nums[j]
            return max(case1, case2)

        n = len(nums)
        m = len(multipliers)
        return dp(0, 0)