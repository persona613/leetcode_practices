"""
37 ms runtime beats 48%
13.9 MB memory beats 74.78%
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for i in range(-1, -len(s)-1, -1):
            if s[i] == " ":
                if ans == 0:
                    continue
                break
            ans += 1
        return ans
                