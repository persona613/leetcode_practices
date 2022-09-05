'''
501ms runtime beats 12.19%
16.2mb memory usage beats 43.39%
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x : abs(x))
        return [n**2 for n in nums]