"""
617 ms runtime beats 78.83%
30.73 MB memory beats 47.97%
"""
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        arr = sorted(nums)
        ans = 0
        for i in range(1, n):
            if arr[i] <= arr[i-1]:
                new_val = arr[i-1] + 1
                ans += new_val - arr[i]
                arr[i] = new_val
        return ans