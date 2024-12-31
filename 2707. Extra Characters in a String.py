"""
188 ms runtime beats 75.13%
16.65 MB memory beats 63.57%
"""
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for word in dictionary:
                if word == s[i - len(word):i]:
                    # make s with curr word if optimal
                    if dp[i - len(word)] < dp[i]:
                        dp[i] = dp[i - len(word)]
                        cw = word
        return dp[-1]