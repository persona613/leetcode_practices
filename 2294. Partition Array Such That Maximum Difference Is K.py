"""
669 ms runtime beats 81.12%
31.27 MB memory beats 16.96%
"""
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        arr = sorted(nums)
        ans = 1
        mi = arr[0]
        for a in arr[1:]:
            if a > mi + k:
                ans += 1
                mi = a
        return ans