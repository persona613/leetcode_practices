"""
54 ms runtime beats 92.58%
18.13 MB memory beats 12.36%
"""    
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cts = []
        for i in range(n):
            d = abs(ord(s[i]) - ord(t[i]))
            cts.append(d)

        l = cost = ans = 0
        for r in range(n):
            cost += cts[r]
            if cost > maxCost:
                cost -= cts[l]
                l += 1
        return r - l + 1