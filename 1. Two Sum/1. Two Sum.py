'''
Runtime: 125 ms, faster than 67.29% of Python3 online submissions 
Memory Usage: 15.2 MB, less than 54.36% of Python3 online submissions
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dic:
                return [dic[diff], i]
            else:
                dic[n] = i