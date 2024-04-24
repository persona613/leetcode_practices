"""
119 ms runtime beats 82.97%
18.29 MB memory beats 7.73%
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        bag = set(nums)
        for i in range(n+1):
            if i not in bag:
                return i
