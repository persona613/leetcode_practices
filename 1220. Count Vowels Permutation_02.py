"""
Memory Limit Exceeded
52 / 64 testcases passed
submitted at May 09, 2024 21:26

Last Executed Input
Use Testcase
n =
14456
"""
class Solution:
    def countVowelPermutation(self, n: int) -> int:

        @lru_cache(None)
        def dp(i, c):
            if i == 1:
                return 1
            
            if c == "a":
                return dp(i - 1, "e") + dp(i - 1, "u") \
                       + dp(i - 1, "i")
            elif c == "e":
                return dp(i - 1, "a") + dp(i - 1, "i")
            elif c == "i":
                return dp(i - 1, "e") + dp(i - 1, "o")
            elif c == "o":
                return dp(i - 1, "i")
            else:
                return dp(i - 1, "o") + dp(i - 1, "i")
        
        ans = 0
        for c in "aeiou":
            ans += dp(n, c)
        return ans % (10 ** 9 + 7)

        