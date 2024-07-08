"""
86 ms runtime beats 96.10%
18.52 MB memory beats 47.65%
"""
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        # i=number of dices(1-index)
        @lru_cache(None)
        def dp(i, cursum):
            if cursum < i or cursum > i * k:
                return 0
            if i == 1 or i * k == cursum:
                return 1
            
            cnt = 0
            for t in range(1, k + 1):
                if cursum - t <= 0:
                    break
                cnt += dp(i - 1, cursum - t) % mod
            return cnt % mod

        mod = 10 ** 9 + 7
        return dp(n, target) % mod