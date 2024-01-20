"""
824 ms runtime beats 83.52%
23.85 MB memory beats 82.12%
"""
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        arr = sorted(nums, reverse=True)
        ans = 0
        cnt = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                ans += cnt
            cnt += 1
        return ans
        