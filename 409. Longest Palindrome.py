"""
52 ms runtime beats 5.81%
16.3 MB memory beats 6.56%
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = defaultdict(int)
        ans = 0
        for c in s:
            dic[c] += 1
            if dic[c] == 2:
                ans += 2
                dic[c] -= 2
        if len(s) > ans:
            ans += 1
        return ans
