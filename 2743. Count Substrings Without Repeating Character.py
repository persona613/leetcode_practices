"""
471 ms runtime beats 71.87%
17.54 MB memory beats 35.42%
"""
class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        ans = 0
        # l = (right-most) left end of spcial array
        l = -1
        bag = dict()
        for r in range(len(s)):
            curr = s[r]
            if curr in bag:
                # left index take right most
                l = max(l, bag[curr])

            # special array count end at r
            ans += r - l
            bag[curr] = r
        return ans