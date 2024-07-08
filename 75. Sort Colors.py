"""
40 ms runtime beats 36.00%
16.47 MB memory beats 79.02%
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l = red index, r = blue index
        l = i = 0
        r = len(nums) - 1
        while i <= r:
            curr = nums[i]
            if curr == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif curr == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1
        