'''
Runtime: 62 ms, faster than 35.37% of Python3 online submissions
Memory Usage: 13.9 MB, less than 0% of Python3 online submissions
'''
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxindex = None
        maxnum = 0
        
        for i in range(len(nums)):
            if nums[i] > maxnum:
                maxnum = nums[i]
                maxindex = i
        for n in nums:
            if n != maxnum and maxnum < n*2:
                return -1
        return maxindex