'''
Runtime: 516 ms, faster than 30.12% of Python3 online submissions 
Memory Usage: 29.6 MB, less than 0% of Python3 online submissions
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        dic = {}
        for i, val in enumerate(nums):
            pos = (i+k)%n
            dic[pos] = val
        for i in range(n):
            nums[i] = dic[i]