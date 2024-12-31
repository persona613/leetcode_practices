"""
829 ms runtime beats 48.98%
282.44 MB memory beats 38.78%
"""
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        # pre calculate all coins are heads or tails
        heads = [1]
        tails = [1]
        for p in prob:
            heads.append(p * heads[-1])
            tails.append((1 - p) * tails[-1])
        
        # dp(index, heads count)
        @lru_cache(None)
        def dp(i, j):
            # if heads count > coins having
            if i < 0 or j > i + 1:
                return 0
            # all heads
            if i + 1 == j:
                return heads[j]
            # all tails:
            if j == 0:
                return tails[i + 1]
            
            # if curr ith coin is head
            p1 = prob[i] * dp(i - 1, j - 1)
            # if curr ith coin is tail
            p2 = (1 - prob[i]) * dp(i - 1, j)
            return p1 + p2
        
        return dp(n - 1, target)