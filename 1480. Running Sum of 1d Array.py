"""
43 ms runtime beats 75.40%
16.66 MB memory beats 6.32%
"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        for v in nums[1:]:
            res.append(v + res[-1])
        return res