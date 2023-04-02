"""
40 ms runtime beats 28.89%
14.2 MB memory beats 14.73%
"""
class Solution:
    def rob(self, nums: List[int]) -> int: 
        # prefix DP, r = rob or not rob house[i]
        def house(i, r):
            if (i, r) in memo: 
                return memo[(i, r)]
            if i == 0: 
                memo[(0, 1)] = nums[0]
                memo[(0, 0)] = 0
                return memo[(i, r)]
            memo[(i, 1)] = house(i-1, 0)+nums[i]
            memo[(i, 0)] = max(house(i-1, 1), house(i-1, 0))
            return memo[(i, r)]
        memo = {}
        n = len(nums)        
        return max(house(n-1, 0), house(n-1, 1))


