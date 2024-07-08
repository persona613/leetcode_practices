"""
533 ms runtime beats 64.20%
30.32 MB memory beats 43.83%
"""
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        # [1,2,3] -> sum reach 6, next optimal int to make is 7
        coins.sort()
        nxt = 1
        i = ans = 0
        ln = len(coins)
        while i < ln:
            if coins[i] > nxt:
                nxt += nxt
                ans += 1
            else:
                nxt += coins[i]
                i += 1
            if nxt > target:
                return ans
        
        while nxt <= target:
            nxt += nxt
            ans += 1
        return ans