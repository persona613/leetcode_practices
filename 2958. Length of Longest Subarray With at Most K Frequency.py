"""
10.57 ms runtime beats 98.25%
31.10 MB memory beats 74.68%
"""
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = defaultdict(int)
        i = j = 0
        ans = 0
        for j in range(n):
            a = nums[j]
            d[a] += 1
            if d[a] > k and j - i > ans:
                ans = j - i
            while d[a] > k:
                d[nums[i]] -= 1
                i += 1
        return max(ans, n - i)
        