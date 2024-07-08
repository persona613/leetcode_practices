"""
528 ms runtime beats 5.33%
19.44 MB memory beats 88.25%
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt0 = l = ans = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                cnt0 += 1
            
            while cnt0 >= 2:
                if nums[l] == 0:
                    cnt0 -= 1
                l += 1

            # no matter cnt0 is 1 or 0 
            # ln = r - l + 1 - 1
            ans = max(ans, r - l)
        return ans