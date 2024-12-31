"""
1173 ms runtime beats 76.65%
18.07 MB memory beats 88.32%
"""
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        mat = [[inf] * 26 for _ in range(26)]
        # init self node
        for i in range(26):
            mat[i][i] = 0

        base = ord("a")
        for u, v, w in zip(original, changed, cost):
            u = ord(u) - base
            v = ord(v) - base
            if mat[u][v] > w:
                mat[u][v] = w
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if mat[i][j] > mat[i][k] + mat[k][j]:
                        mat[i][j] = mat[i][k] + mat[k][j]
        ans = 0
        for u, v in zip(source, target):
            u = ord(u) - base
            v = ord(v) - base
            if mat[u][v] == inf:
                return -1
            ans += mat[u][v]
        return ans