"""
Wrong Answer
121 / 124 testcases passed
Editorial
Input
s = "a"

Use Testcase
Output 0
Expected 1
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = defaultdict(int)
        l = ans = 0
        for r in range(len(s)):
            d[s[r]] += 1
            if len(d) == 2:
                ans = max(ans, r - l + 1)
            elif len(d) > 2:
                if d[s[l]] == 1:
                    del d[s[l]]
                else:
                    d[s[l]] -= 1
                l += 1
        return ans