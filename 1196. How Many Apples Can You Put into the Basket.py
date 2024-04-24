"""
90 ms runtime beats 71.62%
16.74 MB memory beats 52.04%
"""
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        app = sorted(weight)
        ans = 0
        wt = 5000
        for a in app:
            if a > wt:
                break
            wt -= a
            ans += 1
        return ans