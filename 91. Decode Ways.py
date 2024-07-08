"""
42 ms runtime beats 18.99%
16.84 MB memory beats 10.19%
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        
        # curr seperate with or connect to pre
        # dp(i) = dp(i - 1) + dp(i - 2)
        @lru_cache(None)
        def dp(i):
            if i == -1:
                return 1
            if i == 0:
                return 0 if s[i] == "0" else 1
            
            cnt = 0
            # curr seperate with pre
            if s[i] != "0":
                cnt += dp(i - 1)
            # curr connect to pre
            if s[i - 1] != "0" and int(s[i - 1: i + 1]) <= 26:
                cnt += dp(i - 2)
            return cnt
        
        return dp(len(s) - 1)