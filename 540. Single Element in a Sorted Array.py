"""
135 ms runtime beats 78.91%
26.67 MB memory beats 64.88%
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            i = (l + r) // 2
            v = nums[i]
            # i is second element
            if i > 0 and nums[i - 1] == v:
                if i % 2:
                    l = i + 1
                else:
                    r = i - 2
            # i is first element
            elif i < n - 1 and nums[i + 1] == v:
                if i % 2:
                    r = i - 1
                else:
                    l = i + 2
            else:
                return nums[i]
        return nums[l]