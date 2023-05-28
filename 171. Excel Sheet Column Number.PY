"""
38 ms runtime beats 36.47%
13.8 MB memory beats 42.69%
"""
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # ascii 'A'=65,'Z'=90
        ans = 0
        p = len(columnTitle)-1
        for d in columnTitle:
            num = ord(d) - 64
            ans += 26**p * num
            p -= 1
        return ans
