"""
161 ms runtime beats 32.72%
17.59 MB memory beats 93.96%
"""
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1]*nums[-2] - nums[0]*nums[1]