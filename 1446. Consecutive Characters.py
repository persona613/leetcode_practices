"""
49 ms runtime beats 45.63%
16.23 MB memory beats 36.64%
"""
class Solution:
    def maxPower(self, s: str) -> int:
        ans = cnt = 0
        char = s[0]
        for c in s:
            if c != char:
                ans = max(ans, cnt)
                char = c
                cnt = 0
            cnt += 1
        return max(ans, cnt)