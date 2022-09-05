'''
runtime beats 43.76%
memory usage beats 17.8%
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = [n**2 for n in nums]
        return sorted(new)