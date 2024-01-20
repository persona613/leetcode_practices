"""
46 ms runtime beats 41.51%
16.37 MB memory beats 9.46%
"""
class Solution:
    def maxScore(self, s: str) -> int:
        sc = s.count("1")
        ans = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                sc += 1
            else:
                sc -= 1
            if sc > ans:
                ans = sc
        return ans
