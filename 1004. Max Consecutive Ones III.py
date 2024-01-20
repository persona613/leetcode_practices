"""
484 ms runtime beats 74.43%
17.18 MB memory beats 16.41%
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = l = zt = 0        
        for r in range(len(nums)):
            if nums[r] == 0:
                zt += 1
            while zt > k:
                if nums[l] == 0:
                    zt -= 1
                l += 1
            if r - l + 1 > ans:
                ans = r - l + 1
        return ans
        