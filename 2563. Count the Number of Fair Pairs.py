"""
162 ms runtime beats 69.64%
30.80 MB memory beats 61.70%
"""
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        arr = sorted(nums)
        ans = 0
        for i in range(n - 1):
            r = bisect.bisect_right(arr, upper - arr[i], i + 1)
            if r == i + 1:
                break
            l = bisect.bisect_left(arr, lower - arr[i], i + 1)
            ans += r - l
        return ans