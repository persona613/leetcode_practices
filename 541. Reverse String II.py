"""
43 ms runtime beats 50.37%
16.5 MB memory beats 33.88%
"""
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k == 1: return s
        if len(s) <= k : return s[::-1]
        i = 0
        ans = ""
        while i+2*k <= len(s):
            ans += s[i:i+k][::-1] + s[i+k:i+2*k]
            i += 2*k
        if len(s) - i <= k:
            return ans + s[i:i+k][::-1]
        else:
            return ans + s[i:i+k][::-1] + s[i+k:]