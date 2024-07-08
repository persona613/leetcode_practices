"""
36 ms runtime beats 82.72%
16.60 MB memory beats 48.53%
"""
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l = 0
        n = r = len(nums)
        arr = sorted(nums)
        while l <= r:
            mid = (l + r) // 2
            i = bisect.bisect_left(arr, mid)
            cnt = n - i
            if cnt == mid:
                return mid
            elif cnt > mid:
                l = mid + 1
            else:
                r = mid - 1
        return -1