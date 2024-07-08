"""
32 ms runtime beats 84.56%
16.68 MB memory beats 11.64%
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def live(i, j):
            k = 0
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                k += valid(ni, nj)

            curr = board[i][j] % 2
            if (curr == 1 and 2 <= k <= 3) \
                    or (curr == 0 and k == 3):
                return True
            return False

        def valid(i, j):
            if 0 <= i < m and 0 <= j < n:
                return board[i][j] % 2
            return 0

        m = len(board)
        n = len(board[0])
        dirs = list(zip((0,1,0,-1,1,1,-1,-1), (1,0,-1,0,1,-1,-1,1)))
        for i in range(m):
            for j in range(n):
                if live(i, j):
                    board[i][j] += 2
        for i in range(m):
            for j in range(n):
                board[i][j] //= 2