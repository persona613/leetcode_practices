"""
36 ms runtime beats 77.94%
16.37 MB memory beats 29.81%
"""
class Solution:
    def freqAlphabets(self, s: str) -> str:
        # ord("a") = 97
        dic = {i:chr(i+96) for i in range(1, 27)}
        res = []
        i = len(s)-1
        while i >= 0:
            c = s[i]
            if c == "#":
                res.append(dic[int(s[i-2:i])])
                i -= 3
            else:
                res.append(dic[int(c)])
                i -= 1
        return "".join(res[::-1])