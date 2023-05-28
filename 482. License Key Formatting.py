"""
84 ms runtime beats 25.12%
19.8 MB memory beats 5.13%
"""
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        lst = []
        tmp = []
        for i in range(-1, -len(s)-1, -1):
            if s[i] != "-":
                tmp.append(s[i].upper())
            if len(tmp) == k:
                lst.append("".join(tmp[::-1]))
                tmp = []
        if tmp:
            lst.append("".join(tmp[::-1]))
        return "-".join(lst[::-1])