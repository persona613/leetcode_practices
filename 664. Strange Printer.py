"""
788 ms runtime beats 17.59%
20.74 MB memory beats 5.84%
"""
class Solution:
    def strangePrinter(self, s: str) -> int:

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 1
            if s[j] == s[j - 1]:
                return dp(i, j - 1)
            if s[i] == s[i + 1]:
                return dp(i + 1, j)
            
            if s[i] == s[j]:
                return dp(i, j - 1)

            mi = 1 + dp(i, j - 1)
            for k in range(i, j):
                t = dp(i, k) + dp(k + 1, j)
                if t < mi:
                    mi = t
            return mi

        n = len(s)
        return dp(0, n - 1)