"""
96 ms runtime beats 63.88%
17.67 MB memory beats 31.34%
"""
class Solution:
    def minimumSteps(self, s: str) -> int:
        # zero_count meet backward
        cnt = ans = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                cnt += 1
            else:
                ans += cnt
        return ans
        