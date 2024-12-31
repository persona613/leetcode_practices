"""
502 ms runtime beats 39.07%
20.84 MB memory beats 7.28%
"""
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dp(i, m) = Alice score
        # m > 0: Alice turn, take Max
        # m < 0: Bob turn, take Min
        @lru_cache(None)
        def dp(i, m):
            if i >= n:
                return 0

            # take at most: i + 2 * m
            right = min(i + 2 * abs(m), n)

            if m < 0:
                min_score = float("inf")
                for j in range(i, right):
                    score = dp(j + 1, max(abs(m), j - i + 1))
                    min_score = min(min_score, score)
                return min_score
            else:
                max_score = curr_score = 0
                for j in range(i, right):
                    curr_score += piles[j]
                    score = curr_score + \
                            dp(j + 1, -1 * max(m, j - i + 1))
                    max_score = max(max_score, score)
                return max_score

        n = len(piles)
        return dp(0, 1)