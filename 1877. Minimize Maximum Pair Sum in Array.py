"""
972 ms runtime beats 77.29%
30.94 MB memory beats 7.66%
"""
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = i = 0
        j = len(nums)-1
        while i < j:
            t = nums[i]+nums[j]
            if t > ans:
                ans = t
            i += 1
            j -= 1
        return ans