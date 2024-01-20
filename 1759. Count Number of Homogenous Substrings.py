"""
87 ms runtime beats 96.04%
17.62 MB memory beats 11.87%
"""
class Solution:
    def countHomogenous(self, s: str) -> int:
        md = 10**9+7
        ans = cnt = 0
        k = s[0]
        for c in s:
            if c != k:
                ans += cnt*(cnt+1)//2 % md
                k = c
                cnt = 0
            cnt += 1
        ans += cnt*(cnt+1)//2 % md
        return ans % md
            