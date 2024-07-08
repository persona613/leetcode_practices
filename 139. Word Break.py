"""
44 ms runtime beats 32.31%
16.67 MB memory beats 63.38%
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @lru_cache(None)
        def dp(i):
            if i < 0:
                return True
            
            for word in wordDict:
                n = len(word)
                if s[i - n + 1: i + 1] == word \
                        and dp(i - n):
                    return True
            return False
        
        return dp(len(s) - 1)