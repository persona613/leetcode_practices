"""
43 ms runtime beats 5.28%
16.66 MB memory beats 10.80%
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = list(str(num))
        n = len(arr)

        # suf[i] = max element's index in arr[i:]
        suf = [None] * n
        suf[-1] = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[suf[i + 1]]:
                suf[i] = i
            else:
                suf[i] = suf[i + 1]
        
        for i in range(n - 1):
            if arr[i] < arr[suf[i]]:
                arr[i], arr[suf[i]] = arr[suf[i]], arr[i]
                break
        return int("".join(arr))