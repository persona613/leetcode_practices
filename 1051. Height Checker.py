'''
Runtime: 62 ms, faster than 62.26% of Python3 online submissions 
Memory Usage: 13.8 MB, less than 58.38% of Python3 online submissions 
'''
class Solution:
    def bubble(self, heights):
        nums = heights.copy()
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    swapped = True
        return nums
    def heightChecker(self, heights: List[int]) -> int:
        nums = self.bubble(heights)
        cnt = 0
        for i in range(len(heights)):
            if heights[i] != nums[i]:
                cnt += 1
        return cnt