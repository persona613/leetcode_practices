'''
Runtime: 1099 ms, faster than 18.74% of Python3 online submissions
Memory Usage: 14.3 MB, less than 76.32% of Python3 online submissions
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        memo = [[-1 for s in range(total*2+1)] for i in range(len(nums))]

        def calculate(nums, i, sums, t, memo):
            if i == len(nums):
                if sums == t:
                    return 1
                else:
                    return 0
            else:
                if memo[i][sums] != -1:
                    return memo[i][sums]
                add = calculate(nums, i+1, sums+nums[i], t, memo)
                minus = calculate(nums, i+1, sums-nums[i], t, memo)
                memo[i][sums] = add+minus
                return memo[i][sums]
            
        return calculate(nums, 0, 0, target, memo) 