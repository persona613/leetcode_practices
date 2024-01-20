"""
41 ms runtime beats 57.32%
16.31 MB memory beats 47.48%
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # ts = "balon"
        d = Counter(text)
        return min(d["b"], d["a"], d["l"]//2, d["o"]//2, d["n"])
