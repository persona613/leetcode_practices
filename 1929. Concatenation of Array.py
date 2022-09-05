'''
Runtime: 93 ms, faster than 87.80% of Python3 online submissions for Concatenation of Array.
Memory Usage: 14.2 MB, less than 25.35% of Python3 online submissions for Concatenation of Array.
'''
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n*2
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]