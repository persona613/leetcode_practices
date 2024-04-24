"""
40 ms runtime beats 19.19%
16.62 MB memory beats 19.66%
"""
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target > 1:
            if maxDoubles == 0:
                ans += target - 1
                break
            if target % 2 == 1:
                target -= 1
            else:
                target //= 2
                maxDoubles -= 1
            ans += 1
        return ans