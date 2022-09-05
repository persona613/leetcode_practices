'''
Runtime: 272 ms, faster than 5.94% of Python3 online submissions for Build Array from Permutation.
Memory Usage: 14.3 MB, less than 7.75% of Python3 online submissions for Build Array from Permutation.
'''
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        dic = {}
        for i, n in enumerate(nums):
            dic[n] = nums[n]
        for i, n in enumerate(nums):
            nums[i] = dic[n]
        return nums