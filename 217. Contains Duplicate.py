'''
Runtime: 1238 ms, faster than 5.83% of Python3 online submissions 
Memory Usage: 26 MB, less than 66.48% of Python3 online submissions
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        nset = set(nums)
        n = len(nset)
        if l == n:
            return False
        else:
            return True