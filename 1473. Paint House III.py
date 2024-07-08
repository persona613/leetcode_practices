"""
230 ms runtime beats 96.44%
22.91 MB memory beats 66.01%
"""
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        # j = curr color (1-index)
        @lru_cache(None)
        def dp(i, j, k):
            if k > (i + 1) or k <= 0:
                return inf
            if i == 0:
                if houses[i] != 0:
                    return 0
                elif j == 0:
                    return min(cost[i])
                else:
                    return cost[i][j - 1]
                    

            # pre house's color
            prej = houses[i - 1]

            if j != 0:
                # curr house's cost
                if houses[i] != 0:
                    curcost = 0
                else:
                    curcost = cost[i][j - 1]

                if prej == 0:
                    micost = inf
                    # pre color
                    for pcolor in range(1, n + 1):
                        if pcolor != j:
                            precost = dp(i - 1, pcolor, k - 1)
                        else:
                            precost = dp(i - 1, j, k)
                        micost = min(micost, curcost + precost)
                    return micost

                elif prej != j:
                    return curcost + dp(i - 1, prej, k - 1)
                else: # prej == j
                    return curcost + dp(i -1, j, k)

            else: # j == 0
                if prej == 0:
                    micost = inf
                    # icolor = curr house color
                    for icolor in range(1, n + 1):
                        curcost = cost[i][icolor - 1]
                        for pcolor in range(1, n + 1):
                            if pcolor != icolor:
                                precost = dp(i - 1, pcolor, k - 1)
                            else:
                                precost = dp(i - 1, icolor, k)
                            micost = min(micost, curcost + precost)
                    return micost

                else: # prej != 0
                    micost = inf
                    for icolor in range(1, n + 1):
                        curcost = cost[i][icolor - 1]
                        if icolor != prej:
                            precost = dp(i - 1, prej, k - 1)
                        else:
                            precost = dp(i - 1, prej, k)
                        micost = min(micost, curcost + precost)
                    return micost

        ans = dp(m - 1, houses[m - 1], target)
        return ans if ans != inf else -1