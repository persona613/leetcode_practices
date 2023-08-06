"""
42 ms runtime beats 85.50%
16.2 MB memory beats 75.48%
"""
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        ls, ws = 0, 0
        for c in s:
            ws += widths[ord(c)-97]
            if ws > 100:
                ws = widths[ord(c)-97]
                ls += 1
        return [ls+1, ws]