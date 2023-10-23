"""
43 ms runtime beats 46.88%
16.3 MB memory beats 64.19%
"""
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = ans = 0
        for c in s:
            if c == "L":
                cnt -= 1
            else:
                cnt += 1
            if cnt == 0:
                ans += 1
        return ans