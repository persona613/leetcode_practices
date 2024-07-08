"""
87 ms runtime beats 92.62%
17.06 MB memory beats 10.81%
"""
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat[0])
        q = [] 
        # (1's cnt, index)
        for i, row in enumerate(mat):
            if row[-1] == 1:
                heapq.heappush(q, (n, i))
            else:
                heapq.heappush(q, (row.index(0), i)) # 1's cnt

        res = []
        while len(res) < k:
            res.append(heapq.heappop(q)[1])
        return res