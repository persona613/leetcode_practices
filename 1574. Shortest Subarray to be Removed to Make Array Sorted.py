"""
14 ms runtime beats 59.46%
30.46 MB memory beats 78.50%
"""
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        # pi: prefix array index
        pi = 0
        while pi < n - 1:
            if arr[pi] > arr[pi + 1]:
                break
            pi += 1
        if pi == n - 1:
            return 0

        # si: suffix array index
        si = n - 1
        while si > 0:
            if arr[si - 1] > arr[si]:
                break
            si -= 1

        # max length non-decreasing array
        mxln = max(pi + 1, n - si)
        # merge prefix and suffix array
        for i in range(pi + 1):
            j = bisect.bisect_left(arr, arr[i], si)
            mxln = max(mxln, (i + 1) + (n - j))
        return n - mxln