"""
91 ms runtime beats 31.82%
24.86 MB memory beats 31.10%
"""
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def dfs(i):
            for d in range(0, 10):
                i += d
                if i > n:
                    break
                if i > 0:
                    res.append(i)
                    dfs(i * 10)
                i -= d
        res = []
        dfs(0)
        return res