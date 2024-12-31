"""
192 ms runtime beats 20.37%
19.48 MB memory beats 32.16%
"""
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        keys = dict()
        for row in matrix:
            k1 = "".join(map(str, row))
            keys[k1] = keys.setdefault(k1, 0) + 1

            # flip k1
            tmp = []
            for b in row:
                tmp.append(b ^ 1)
            k2 = "".join(map(str, tmp))
            keys[k2] = keys.setdefault(k2, 0) + 1
        return max(keys.values())