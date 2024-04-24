"""
4585 ms runtime beats 37.36%
16.66 MB memory beats 26.43%
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(i, j, k) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == p:
                return True

            board[i][j] = "#"
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if valid(ni, nj) and board[ni][nj] != "#":
                    if backtrack(ni, nj, k + 1):
                        return True
            board[i][j] = word[k]
            return False

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        dirs = list(zip([0, 0, 1, -1], [1, -1, 0, 0]))
        m = len(board)
        n = len(board[0])
        p = len(word) - 1
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False