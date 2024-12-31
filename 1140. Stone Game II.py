"""
147 ms runtime beats 88.78%
18.20 MB memory beats 67.75%
"""
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dp(i, m) = Curr-Player gain max
        @lru_cache(None)
        def dp(i, m):
            if i >= n:
                return 0

            # can take all piles
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            # find opponent's mini gain
            opp = float("inf")
            for x in range(1, 2 * m + 1):
                gain = dp(i + x, max(m, x))
                opp = min(opp, gain)

            # curr max = max(all_stones - opponent's gain)
            # = all_stones - min(opponent's gain)
            return suffix_sum[i] - opp

        n = len(piles)
        suffix_sum = piles[:]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] += suffix_sum[i + 1]
        return dp(0, 1)