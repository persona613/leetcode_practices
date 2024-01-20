"""
59 ms runtime beats 40.68%
16.29 MB memory beats 64.29%
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)