"""
251 ms runtime beats 8.54%
18.82 MB memory beats 9.37%
"""  
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        q = deque()
        while l <= r:
            if nums[l]**2 >= nums[r]**2:
                q.appendleft(nums[l]**2)
                l += 1
            else:
                q.appendleft(nums[r]**2)
                r -= 1
        return q