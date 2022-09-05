'''
Runtime: 53 ms, faster than 96.23% of Python3 online submissions 
Memory Usage: 15.4 MB, less than 51.2% of Python3 online submissions 
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = set(nums)
        if len(a) >= 3:
            return sorted(list(a), reverse=True)[2]
        return max(nums)
        