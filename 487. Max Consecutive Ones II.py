"""
324 ms runtime beats 66.63%
16.59 MB memory beats 45.71%
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = l = z = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                z += 1
            while z > 1:
                if nums[l] == 0:
                    z -= 1
                l += 1
            if r - l + 1 > ans:
                ans = r - l + 1
        return ans