"""
520 ms runtime beats 68.25%
28.71 MB memory beats 21.94%
"""
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ps = sorted(piles, reverse=True)
        ans = 0
        for i in range(1, len(piles)//3*2+1, 2):
            ans += ps[i]
        return ans
