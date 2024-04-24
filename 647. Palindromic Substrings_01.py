"""
107 ms runtime beats 46.46%
16.63 MB memory beats 46.57%
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        arr = s.replace("", "*")
        print(arr)
        ans = 0
        n = len(arr)
        for i in range(1, n):
            d = 0
            while (i + d < n and i - d >= 0) \
                and arr[i + d] == arr[i - d]:
                d += 1
            ans += d // 2
        return ans