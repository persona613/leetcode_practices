"""
34 ms runtime beats 38.41%
13.9 MB memory beats 43.10%
"""
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        maps = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
        ans = ""
        q = columnNumber
        while q != 0:
            r = q % 26
            ans += maps[r]
            if r == 0:
                q = (q//26) - 1
            else:
                q = q // 26
        return ans[::-1]