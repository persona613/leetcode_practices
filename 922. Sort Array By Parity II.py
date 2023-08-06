"""
169 ms runtime beats 100%
18.7 MB memory beats 69.25%
"""
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # i: scan even index
        i, j, n = 0, 1, len(nums)
        while i < n and j < n:
            while i < n and nums[i] % 2 == 0:
                i += 2
            while j < n and nums[j] % 2 == 1:
                j += 2
            if i >= n or j >= n: break
            nums[i], nums[j] = nums[j], nums[i]
            i += 2
            j += 2
        return nums
