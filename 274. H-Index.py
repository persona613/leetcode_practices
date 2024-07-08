"""
40 ms runtime beats 63.17%
16.90 MB memory beats 57.51%
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        arr = sorted(citations)
        n = len(arr)
        l = 0
        r = min(n, 1000)
        while l <= r:
            mid = (l + r) // 2
            i = bisect.bisect_left(arr, mid)
            if n - i >= mid:
                l = mid + 1
            else:
                r = mid - 1
        return r