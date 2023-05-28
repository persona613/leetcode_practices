"""
158 ms runtime beats 21.37%
18.4 MB memory beats 6.45%
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        bag = set(nums)
        for i in range(n+1):
            try:
                bag.remove(i)
            except:
                return i
