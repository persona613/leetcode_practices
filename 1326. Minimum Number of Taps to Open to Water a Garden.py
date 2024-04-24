"""
113 ms runtime beats 68.31%
18.06 MB memory beats 36.31%
"""
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        arr = []
        for i in range(n + 1):
            d = ranges[i]
            arr.append((i - d, i + d))
        arr.sort()
        i = 0
        rlimit = ans = 0
        while i < n + 1:
            if arr[i][0] <= rlimit:
                tmp_r = arr[i][1]
                j = i + 1
                while j < n + 1:
                    if arr[j][0] <= rlimit:
                        if arr[j][1] > tmp_r:
                            tmp_r = arr[j][1]
                        j += 1
                    else:
                        break
                ans += 1
                i = j
                rlimit = tmp_r
                if rlimit >= n:
                    break
            else:
                i += 1
        return ans if rlimit >= n else -1