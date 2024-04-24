"""
8474 ms runtime beats 5%
259.60 MB memory beats 5.01%
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        # @lru_cache(None)
        def dp(i, tm):
            if tm == 0:
                return 0
            if i == 0:
                return inf
            
            coin = coins[i - 1]
            if tm % coin == 0:
                return tm // coin
            if i == 1:
                return inf

            change_limit = tm // coin
            cnt = inf
            for k in range(1, change_limit + 1):
                ret = k + dp(i - 1, tm - coin * k)
                if ret < cnt:
                    cnt = ret
            return min(dp(i-1, tm), cnt)

        coins.sort()
        ret = dp(len(coins), amount)
        return ret if ret != inf else -1