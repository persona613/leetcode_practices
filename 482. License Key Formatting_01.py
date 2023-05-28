"""
Wrong Answer
2 / 38 testcases passed
Input
s = "2-4A0r7-4k"
k = 4
Output
"2-4A0R-74K"
Expected
"24A0-R74K"
"""
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # first dash index
        fd = s.index("-")
        ans = s[:fd+1].upper()
        cnt = 0
        for i in range(fd+1, len(s)):
            if cnt == k:
                ans += "-"
                cnt = 0
            if s[i] != "-":
                cnt += 1
                ans += s[i].upper()
        return ans