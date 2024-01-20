"""
677 ms runtime beats 86.99%
35.78 MB memory beats 44.61%
"""
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = dict()
        ans = inf
        for i in range(len(cards)):
            # v = cards[i]
            if cards[i] in d:
                ans = min(ans, i - d[cards[i]] + 1)
            d[cards[i]] = i
        return ans if ans != inf else -1