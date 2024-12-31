"""
156 ms runtime beats 97.82%
32.17 MB memory beats 97.75%
"""
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n
        ans = 0
        order = sorted(range(n), key = lambda x: nums[x])
        for idx in order:
            if marked[idx] is False:
                ans += nums[idx]
                marked[idx] = True
                if idx - 1 >= 0:
                    marked[idx - 1] = True
                if idx + 1 < n:
                    marked[idx + 1] = True
        return ans