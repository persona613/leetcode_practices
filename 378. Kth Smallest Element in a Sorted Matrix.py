"""
157 ms runtime beats 47.98%
21.24 MB memory beats 28.57%
"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        # max heap
        q = []
        for i in range(m):
            for j in range(n):
                if len(q) < k:
                    heapq.heappush(q, -matrix[i][j])
                elif matrix[i][j] < -q[0]:
                    heapq.heappop(q)
                    heapq.heappush(q, -matrix[i][j])
                else:
                    break
        return -q[0]