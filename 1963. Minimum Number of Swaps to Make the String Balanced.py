"""
363 ms runtime beats 32.33%
27.94 MB memory beats 45.06%
"""
class Solution:
    def minSwaps(self, s: str) -> int:
        l, r = 0, len(s) - 1
        head = tail = 0
        ans = 0
        while l < r:
            # head run till un-balance: close > open
            while l < r:
                head += 1 if s[l] == "[" else -1
                if head < 0:
                    break
                l += 1
            # tail run till un-balance: open > close
            while l < r:
                tail += 1 if s[r] == "[" else -1
                if tail > 0:
                    break
                r -= 1
            if l >= r: break
                
            # swap
            head += 2
            tail -= 2
            l += 1
            r -= 1
            ans += 1
        return ans