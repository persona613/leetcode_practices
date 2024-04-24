"""
272 ms runtime beats 70.12%
17.74 MB memory beats 88.36%
"""
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = [1] * n
        k -= n
        for i in range(n - 1, -1, -1):
            if k >= 25:
                res[i] += 25
                k -= 25
            else:
                res[i] += k
                break
        base = ord("a") - 1
        for i in range(n):
            res[i] = chr(base + res[i])
        return "".join(res)