"""
118 ms runtime beats 79.10%
16.5 MB memory beats 80.16%
"""
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rs, cs = set(), set()
        for row in matrix:
            rs.add(min(row))
        for col in zip(*matrix):
            cs.add(max(col))
        return rs & cs        