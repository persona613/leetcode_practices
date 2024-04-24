"""Wrong Answer
99 / 100 testcases passed
Input
s =
"cabacbac"

Use Testcase
Output 1
Expected 2
"""
class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                break
            c = s[i]
            while s[i] == c and i + 1 < j:
                i += 1
            while s[j] == c and i + 1 < j:
                j -= 1
            if i + 1 == j:
                return 0 if s[i] == s[j] else 1
        return j - i + 1