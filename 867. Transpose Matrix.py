"""
99 ms runtime beats 9.86%
17.2 MB memory beats 74.46%
"""
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return matrix and [[i for i in row] for row in zip(*matrix)]

