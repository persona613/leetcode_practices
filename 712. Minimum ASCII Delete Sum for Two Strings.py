"""
818 ms runtime beats 20.22%
212.28 MB memory beats 9.04%
"""
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            if i >= m and j >= n:
                return 0
            elif i >= m:
                return sum(ord(c) for c in s2[j:])
            elif j >= n:
                return sum(ord(c) for c in s1[i:])
            
            if s1[i] == s2[j]:
                return dp(i + 1, j + 1)
            else:
                return min(ord(s1[i]) + dp(i + 1, j),
                           ord(s2[j]) + dp(i, j + 1))

        m = len(s1)
        n = len(s2)
        return dp(0, 0)