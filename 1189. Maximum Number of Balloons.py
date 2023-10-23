"""
43 ms runtime beats 64.18%
16.5 MB memory beats 27.96%
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ts = "balon"
        cnt = {k:0 for k in ts}
        for c in text:
            if c in cnt:
                cnt[c] += 1
        cnt["l"] = cnt["l"] // 2
        cnt["o"] = cnt["o"] // 2
        return min(cnt.values())
