'''
Runtime: 293 ms, faster than 5.05% of Python3 online submissions for Build Array from Permutation.
Memory Usage: 14.1 MB, less than 45.73% of Python3 online submissions for Build Array from Permutation.
'''
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        for i in range(n):
            ans[i] = nums[nums[i]]
        return ans