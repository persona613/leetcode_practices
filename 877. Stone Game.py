"""
415 ms runtime beats 19.16%
126.88 MB memory beats 15.78%
"""
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Alice: positive score, odd turn
        # Blob: negtive score, even turn
        @lru_cache(None)
        def dp(l, r):
            if l > r:
                return 0

            # curr turn is odd or even
            turn = l + n - r
            if turn % 2 == 1:
                take_left = piles[l] + dp(l+1, r)
                take_right = piles[r] + dp(l, r-1)
                return max(take_left, take_right)
            else:
                take_left = -1 * piles[l] + dp(l+1, r)
                take_right = -1 * piles[r] + dp(l, r-1)
                return min(take_left, take_right)
                
        n = len(piles)
        ret = dp(0, n-1)
        return True if ret > 0 else False