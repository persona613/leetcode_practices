"""
939 ms runtime beats 79.73%
54.79 MB memory beats 90.16%
"""
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for _, vt in edges:
            indegree[vt] += 1
        return [i for i in range(n) if indegree[i] == 0]