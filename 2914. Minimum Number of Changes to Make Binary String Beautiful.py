"""
18 ms runtime beats 79.73%
16.87 MB memory beats 89.02%
"""
class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                ans += 1
        return ans
        