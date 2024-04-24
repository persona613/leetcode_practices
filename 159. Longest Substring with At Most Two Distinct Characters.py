"""
173 ms runtime beats 93.73%
17.01 MB memory beats 97.31%
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = defaultdict(int)
        l = 0
        for a in s:
            d[a] += 1
            if len(d) > 2:
                if d[s[l]] == 1:
                    del d[s[l]]
                else:
                    d[s[l]] -= 1
                l += 1
        return len(s) - l