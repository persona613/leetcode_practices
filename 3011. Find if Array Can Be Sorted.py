"""
7 ms runtime beats 78.18%
16.68 MB memory beats 43.17%
"""
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        k = nums[0].bit_count()
        currmax = nums[0]
        currmin = nums[0]
        premax = float("-inf")
        for i in range(1, n):
            if nums[i].bit_count() == k:
                currmax = max(currmax, nums[i])
                currmin = min(currmin, nums[i])
            else:
                if premax > currmin:
                    return False
                premax = currmax
                currmax = nums[i]
                currmin = nums[i]
                k = nums[i].bit_count()
        return premax <= currmin