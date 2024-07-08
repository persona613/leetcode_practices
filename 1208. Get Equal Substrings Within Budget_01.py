"""
60 ms runtime beats 98.55%
17.99 MB memory beats 18.46%
"""    
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cts = []
        for i in range(n):
            d = abs(ord(s[i]) - ord(t[i]))
            cts.append(d)

        l = cost = ans = 0
        for r in range(len(s)):
            cost += cts[r]
            while cost > maxCost:
                cost -= cts[l]
                l += 1
            if r - l + 1 > ans:
                ans = r - l + 1
        return ans