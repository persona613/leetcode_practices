"""
304 ms runtime beats 29.08%
25.47 MB memory beats 91.63%
"""
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = []
        curr = 0
        for c in word:
            curr = ((curr * 10) % m + int(c)) % m
            if curr % m == 0:
                res.append(1)
            else:
                res.append(0)
        return res