"""
39 ms runtime beats 97.63%
25.02 MB memory beats 41.30%
"""
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # total sum, negtive value counts
        ts = neg = 0
        mi = 100001
        for row in matrix:
            for v in row:
                ts += abs(v)
                if abs(v) < mi:
                    mi = abs(v)
                if v < 0:
                    neg += 1

        if neg % 2 == 0:
            return ts
        # mi == 0 or neg % 2 == 1
        return ts - mi * 2