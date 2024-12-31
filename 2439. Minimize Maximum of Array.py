"""
550 ms runtime beats 90.06%
29.31 MB memory beats 75.32%
"""
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # max mean
        mx = presum = 0
        for i in range(len(nums)):
            presum += nums[i]
            # mean = sum / size, +i for right-mid
            curr_mean = (presum + i) // (i + 1)
            if curr_mean > mx:
                mx = curr_mean
        return mx