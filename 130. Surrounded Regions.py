"""
127 ms runtime beats 28.76%
17.99 MB memory beats 43.38%
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i, j):
            board[i][j] = "P"
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if valid(ni, nj) and board[ni][nj] == "O":
                    dfs(ni, nj)

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        dirs = list(zip((0, 1, 0, -1), (1, 0, -1, 0)))
        m = len(board)
        n = len(board[0])
        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m - 1][j] == "O":
                dfs(m - 1, j)
        for i in range(1, m - 1):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n - 1] == "O":
                dfs(i, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "P":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"