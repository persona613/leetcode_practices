"""
0 ms runtime beats 100.00%
17.87 MB memory beats 22.32%
"""
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxday = days[-1]
        # is_travel_days
        tdays = [False] * (maxday + 1)
        for d in days:
            tdays[d] = True

        dp = [0] * (maxday + 1)
        for i in range(1, maxday + 1):
            if tdays[i]:
                # buy 1-day pass
                cost1 = dp[i - 1] + costs[0]
                if i >= 7:
                    cost2 = dp[i - 7] + costs[1]
                else:
                    cost2 = costs[1]
                if i >= 30:
                    cost3 = dp[i - 30] + costs[2]
                else:
                    cost3 = costs[2]
                dp[i] = min(min(cost1, cost2), cost3)
            else:
                dp[i] = dp[i - 1]
        return dp[-1]
        