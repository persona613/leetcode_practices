"""
77 ms runtime beats 46.08%
18.97 MB memory beats 60.28%
"""
class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        d = 1 if player % 2 else -1
        self.rows[row] += d
        self.cols[col] += d
        if row + col == self.n - 1:
            self.diag += d
        if row == col:
            self.anti += d

        k = self.n * d
        if k in self.rows or k in self.cols \
                or k == self.diag or k == self.anti:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)