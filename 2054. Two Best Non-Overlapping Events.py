"""
347 ms runtime beats 27.67%
57.49 MB memory beats 61.44%
"""
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        arr = sorted(events)
        n = len(arr)

        # suffix maxmimal values
        suf = [0] * n
        suf[-1] = arr[-1][2]
        for i in range(n - 2, -1, -1):
            suf[i] = max(suf[i + 1], arr[i][2])

        ans = 0
        for i in range(n):
            curr = arr[i][2]
            t = bisect.bisect_right(arr, arr[i][1], key = lambda x: x[0])
            if t < n:
                curr += suf[t]
            ans = max(ans, curr)
        return ans
        