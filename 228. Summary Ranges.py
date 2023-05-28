"""
35 ms runtime beats 33.58%
13.8 MB memory beats 55.82%
"""
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            n = nums[i] + 1
            j = i+1
            while j < len(nums) and nums[j] == n:
                j += 1
                n += 1
            if nums[i] != nums[j-1]:
                res.append(str(nums[i]) + "->" + str(nums[j-1]))
            else:
                res.append(str(nums[i]))
            i = j
        return res