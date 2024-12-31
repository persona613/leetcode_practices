"""
48 ms runtime beats 82.71%
49.03 MB memory beats 35.92%
"""
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        m = len(s)
        n = len(spaces)
        i = j = 0
        while j < n:
            res.append(s[i: spaces[j]])
            res.append(" ")
            i = spaces[j]
            j += 1
        res.append(s[i:])
        return "".join(res)