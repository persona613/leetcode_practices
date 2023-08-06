"""
74 ms runtime beats 36.48%
16.3 MB memory beats 89.91%
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        i, j, t, dup, n = 0, 1, False, 0, len(nums)
        while j < len(nums):
            if nums[i] == nums[j]:
                if not t:
                    j += 1
                    t = True
                else:
                    nums[j] = float("inf")
                    dup += 1
                    j += 1
            else:
                i = j
                j = i+1
                t = False
        nums.sort()
        return n - dup
