"""
916 ms runtime beats 5.56%
36.29 MB memory beats 97.78%
"""
class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        m = len(monsters)
        mc = sorted(map(list, zip(monsters, coins)))
        # presum coins
        for i in range(1, m):
            mc[i][1] += mc[i - 1][1]

        n = len(heroes)
        res = [0] * n
        for i in range(n):
            l = 0
            r = m - 1
            while l <= r:
                mid = (l + r) // 2
                if mc[mid][0] > heroes[i]:
                    r = mid - 1
                else:
                    l = mid + 1
            if r >= 0:
                res[i] = mc[r][1]
        return res