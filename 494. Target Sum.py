'''
Runtime: 145 ms, faster than 67.84% of Python3 online submissions
Memory Usage: 43.91 MB, less than 10.36% of Python3 online submissions
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # index, curr sum
        @lru_cache(None)
        def dfs(i, csum):
            if i == len(nums):
                return 1 if csum == target else 0

            add = dfs(i + 1, csum + nums[i])
            neg = dfs(i + 1, csum - nums[i])
            return add + neg

        self.total_sum = sum(nums)
        if abs(target) > self.total_sum:
            return 0
        return dfs(0, 0)