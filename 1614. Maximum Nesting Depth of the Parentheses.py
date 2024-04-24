"""
38 ms runtime beats 37.13%
16.57 MB memory beats 38.30%
"""
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = cnt = 0
        for c in s:
            if c == "(":
                cnt += 1
                if cnt > ans:
                    ans = cnt
            elif c == ")":
                cnt -= 1
        return ans