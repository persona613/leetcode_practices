"""
37 ms runtime beats 91.02%
17.78 MB memory beats 8.46%
"""
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        @lru_cache(None)
        def dp(i):
            if i > maxday:
                return 0
            if i not in tdays:
                return dp(i + 1)
            
            micost = float("inf")
            for k in range(3):
                cost = costs[k] + dp(i + passes[k])
                if cost < micost:
                    micost = cost
            return micost

        maxday = max(days)
        tdays = set(days)
        passes = [1, 7, 30]
        return dp(0)