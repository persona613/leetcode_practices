'''
Runtime: 477 ms, faster than 65.51% of Python3 online submissions 
Memory Usage: 26.3 MB, less than 16.83% of Python3 online submissions 
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = set(nums)
        b = set(range(1, len(nums)+1))
        return list(b-a)