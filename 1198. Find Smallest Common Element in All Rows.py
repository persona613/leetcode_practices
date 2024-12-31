"""
375 ms runtime beats 66.78%
41.50 MB memory beats 64.71%
"""
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        cads = deque(mat[0])
        m = len(mat)
        n = len(mat[0])
        for i in range(1, m):
            if not cads:
                return -1

            # binary search start index
            j = 0
            for _ in range(len(cads)):
                curr = cads.popleft()
                j = bisect.bisect_left(mat[i], curr, j, n - 1)
                if j == n:
                    continue
                if mat[i][j] == curr:
                    cads.append(curr)
                    j += 1
        return min(cads) if cads else -1