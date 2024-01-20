"""
Wrong Answer
6 / 54 testcases passed
Editorial
Input
s = "cabbac"
Use Testcase
Output 0
Expected 4
"""
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = defaultdict()
        ans = inf
        for i in range(len(s)):
            if s[i] in d:
                ans = min(ans, i - d[s[i]] - 1)
            d[s[i]] = i
        return -1 if ans == inf else ans