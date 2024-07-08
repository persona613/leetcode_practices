"""
340 ms runtime beats 88.61%
17.76 MB memory beats 78.40%
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # left most save point
        sp = len(nums) - 1
        for i in range(sp, -1, -1):
            # jump farest point
            jp = i + nums[i]
            if jp >= sp:
                sp = i
        return sp == 0