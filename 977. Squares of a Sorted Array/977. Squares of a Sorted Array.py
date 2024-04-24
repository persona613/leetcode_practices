"""
148 ms runtime beats 89.18%
19.04 MB memory beats 35.01%
"""  
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [None] * n
        l = 0
        r = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                sq = nums[l]
                l += 1
            else:
                sq = nums[r]
                r -= 1
            res[i] = sq * sq
        return res
