"""
53 ms runtime beats 12.97%
16.3 MB memory beats 52.13%
"""
class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i].isupper():
                s[i] = s[i].lower()
        return "".join(s)        