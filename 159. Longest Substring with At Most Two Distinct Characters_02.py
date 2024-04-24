"""
174 ms runtime beats 99.25%
17.88 MB memory beats 12.38%
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = defaultdict(int)
        l = ans = 0
        for r in range(len(s)):
            d[s[r]] += 1
            if len(d) <= 2:
                ans = max(ans, r - l + 1)
            else:
                if d[s[l]] > 1:
                    d[s[l]] -= 1
                else:
                    del d[s[l]]
                l += 1
        return ans