"""
332 ms runtime beats 92.90%
22.22 MB memory beats 49.35%
"""
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # (values[i] + i) + (values[j] - j)
        premax = 0
        score = 0
        for j, v in enumerate(values):
            if premax + v - j > score:
                score = premax + v - j
            premax = max(premax, v + j)
        return score
        