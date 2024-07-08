"""
702 ms runtime beats 36.10%
321.85 MB memory beats 5.05%
"""
class Solution:
    def countVowelPermutation(self, n: int) -> int:

        @lru_cache(None)
        def dp(i, c):
            if i == 1:
                return 1
            
            if c == "a":
                return (dp(i - 1, "e") + dp(i - 1, "u") \
                       + dp(i - 1, "i")) % mod
            elif c == "e":
                return (dp(i - 1, "a") + dp(i - 1, "i")) % mod
            elif c == "i":
                return (dp(i - 1, "e") + dp(i - 1, "o")) % mod
            elif c == "o":
                return dp(i - 1, "i") % mod
            else:
                return (dp(i - 1, "o") + dp(i - 1, "i")) % mod
        
        mod = 10 ** 9 + 7
        ans = 0
        for c in "aeiou":
            ans += dp(n, c)
        return ans % mod        