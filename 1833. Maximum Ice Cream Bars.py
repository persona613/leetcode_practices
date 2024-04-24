"""
635 ms runtime beats 58.83%
30.52 MB memory beats 15.05%
"""
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cts = sorted(costs)
        money = coins
        for i in range(len(cts)):
            cost = cts[i]
            if money < cost:
                break
            money -= cost
        else:
            return i + 1
        return i