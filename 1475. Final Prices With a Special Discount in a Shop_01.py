"""
53 ms runtime beats 71.47%
16.26 MB memory beats 85.83%
"""
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        mp = [0] * len(prices)
        stk = []
        for i, p in enumerate(prices):
            while stk and stk[-1][1] >= p:
                mp[stk.pop()[0]] = p
            stk.append((i, p))
        # res = []
        # for p, d in zip(prices, mp):
        #     res.append(p-d)
        # return res
        return map(lambda x: x[0]-x[1], zip(prices,mp))