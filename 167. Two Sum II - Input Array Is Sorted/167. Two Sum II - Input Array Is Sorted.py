'''
Runtime: 215 ms, faster than 69.74% of Python3 online submissions 
Memory Usage: 14.8 MB, less than 89.83% of Python3 online submissions
'''
class Solution:
    def bs(self, nums, t):
        l = 0
        r= len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == t:
                return m
            elif nums[m] < t:
                l = m+1
            elif nums[m] > t:
                r = m-1
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            t = target - v
            if numbers[k+1] == t:
                return [k+1, k+2] # 1-index
            elif self.bs(numbers, t):
                return [k+1, self.bs(numbers, t)+1] # 1-index
            