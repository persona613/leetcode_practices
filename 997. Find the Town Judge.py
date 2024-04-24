"""
594 ms runtime beats 83.67%
21.54 MB memory beats 86.28%
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
        ind = [0] * (n + 1)
        out = [0] * (n + 1)
        for a, b in trust:
            out[a] += 1
            ind[b] += 1
        for i in range(1, n + 1):
            if ind[i] == n - 1 and out[i] == 0:
                return i
        return -1
