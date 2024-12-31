"""
1543 ms runtime beats 81.62%
16.74 MB memory beats 25.74%
"""
class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        board = [[-1] * n for _ in range(m)]
        board[r][c] = 0
        dirs = [[1, 2], [2, 1], [-1, 2], [-2, 1], [-1, -2], [-2, -1], [1, -2], [2, -1]]
        cells_count = m * n
        # cells seen count
        seen = [1]
        
        # curr_row, curr_col
        def backtrack(board, cr, cc, seen):
            if seen[0] == cells_count:
                return board

            for dr, dc in dirs:
                nr = cr + dr
                nc = cc + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n \
                    or board[nr][nc] >= 0:
                    continue
                board[nr][nc] = seen[0]
                seen[0] += 1
                if backtrack(board, nr, nc, seen):
                    return board
                board[nr][nc] = -1
                seen[0] -= 1

        # constraints guarantee at least one possible order
        return backtrack(board, r, c, seen)
