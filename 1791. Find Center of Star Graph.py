"""
644 ms runtime beats 85.52%
52.22 MB memory beats 58.68%
"""
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return set(edges[0]).intersection(set(edges[1])).pop()