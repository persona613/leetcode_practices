'''
Runtime: 211 ms, faster than 98.57% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.2 MB, less than 49.39% of Python3 online submissions for Squares of a Sorted Array.
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([n*n for n in nums])
# n*n seems faster than n**2


'''
runtime beats 56%
memory usage beats 49.44%
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([n**2 for n in nums])