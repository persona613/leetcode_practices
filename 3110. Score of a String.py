"""
39 ms runtime beats 41.43%
16.52 MB memory beats 30.64%
"""
class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            ans += abs(ord(s[i]) - ord(s[i-1]))
        return ans