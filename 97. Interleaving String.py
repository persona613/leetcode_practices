"""
31 ms runtime beats 96.45%
17.36 MB memory beats 26.51%
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @lru_cache(None)
        def dp(i, j):
            if i + j == m + n:
                return True

            curr = s3[i + j]
            if i < m and curr == s1[i] and dp(i + 1, j):
                return True
            if j < n and curr == s2[j] and dp(i, j + 1):
                return True
            return False

        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        return dp(0, 0)