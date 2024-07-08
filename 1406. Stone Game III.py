"""
4381 ms runtime beats 6.35%
473.61 MB memory beats 5.34%
"""
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # Alice: p=0, max score, take max
        # Bob: p=1, negtive score, take min
        @lru_cache(None)
        def dp(p, i):
            if i >= n:
                return 0

            res = float("-inf") if p == 0 else float("inf")
            take = 0
            for d in range(1, 4):
                if i + d > n:
                    break
                if p == 0:
                    take += stoneValue[i + d - 1]
                    score = take + dp(p ^ 1, i + d)
                    res = max(res, score)
                else:
                    take -= stoneValue[i + d - 1]
                    score = take + dp(p ^ 1, i + d)
                    res = min(res, score)
            return res

        n = len(stoneValue)
        score = dp(0, 0)
        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"