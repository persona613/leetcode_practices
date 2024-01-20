"""
67 ms runtime beats 89.57%
17.21 MB memory beats 22.76%
"""
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)