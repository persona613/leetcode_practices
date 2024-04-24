"""
52 ms runtime beats 65.45%
16.71 MB memory beats 64.63%
"""
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens: return 0
        tks = sorted(tokens)
        n = len(tks)
        l = score = 0
        r = len(tks) - 1
        while l <= r:
            if score > 0:
                power += tks[r]
                score -= 1
                r -= 1
                # print(f"power:{power}, r:{r}, score:{score}")
            while l < n and power >= tks[l]:
                power -= tks[l]
                score += 1
                l += 1
                # print(f"power:{power}, l:{l}, score:{score}")
            if l >= r or l == 0:
                break
        return score