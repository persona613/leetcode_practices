'''
Runtime: 631 ms, faster than 10.24% of Python3 online submissions
Memory Usage: 16.9 MB, less than 19.97% of Python3 online submissions
'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        new = sorted(nums)
        pairmin = [v for i, v in enumerate(new) if i%2 == 0 ]
        return sum(pairmin)