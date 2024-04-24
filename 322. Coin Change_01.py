"""
1363 ms runtime beats 85.39%
42.3 MB memory beats 9.10%
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # tm = total money, cnt = coins number
        # C(tm) = C(tm-val) + 1
        def take(tm):
            if tm in memo:
                return memo[tm]  
            if tm < 0:
                return float("inf")
            if tm == 0:
                return 0

            tmp = []
            for val in coins:
                ret = take(tm-val)
                tmp.append(ret+1)
            memo[tm] = min(tmp)
            return memo[tm]

        # {tm: cnt}
        memo = defaultdict(int)
        ret = take(amount)
        if ret != float("inf"):
            return ret
        else: return -1