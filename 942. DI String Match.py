"""
61 ms runtime beats 96.21%
17.62 MB memory beats 67.38%
"""
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        hi = len(s)
        lo = 0
        res = []
        for c in s:
            if c == "I":
                res.append(lo)
                lo += 1
            else:
                res.append(hi)
                hi -= 1
        res.append(lo)
        return res
