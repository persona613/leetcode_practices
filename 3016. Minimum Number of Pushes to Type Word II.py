"""
151 ms runtime beats 65.39%
17.54 MB memory beats 73.03%
"""
class Solution:
    def minimumPushes(self, word: str) -> int:
        feq = sorted(Counter(word).values(), reverse = True)
        ans = 0
        for i, v in enumerate(feq):
            ans += v * (i // 8 + 1)
        return ans