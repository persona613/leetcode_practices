"""
877 ms runtime beats 59.16%
30.94 MB memory beats 56.87%
"""
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        t = max(nums)
        j = cnt = ans = 0
        for i in range(n):
            if nums[i] == t:
                cnt += 1
            while cnt >= k:
                ans += n - i
                if nums[j] == t:
                    cnt -= 1
                j += 1
        return ans