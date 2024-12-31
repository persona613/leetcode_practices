"""
Time Limit Exceeded
14 / 24 testcases passed
"""
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m = len(board)
        n = len(board[0])
        while True:
            # candy cursh position
            remove = [[False] * n for _ in range(m)]
            if self.state(board, m, n, remove):
                break
            self.crush(board, m, n, remove)
            self.gravity(board, m, n)
        return board

    def state(self, board, m, n, remove):
        # init state is stable
        stable = True
        # row-wise, i=row, j=col
        # scan and mark [start:end] for crush
        for i in range(m):
            curr_candy = None
            cnt = 0
            mark = []
            for j in range(n):
                if board[i][j] == 0:
                    continue
                if board[i][j] != curr_candy:
                    if cnt >= 3:
                        mark.append([j - cnt, j])
                        stable = False
                    curr_candy = board[i][j]
                    cnt = 1
                else:
                    cnt += 1
            if cnt >= 3:
                mark.append([n - cnt, n])
                stable = False
            # mark for remove after
            for pair in mark:
                for j in range(pair[0], pair[1]):
                    remove[i][j] = True

        # col-wise, i=row, j=col
        for j in range(n):
            curr_candy = None
            cnt = 0
            mark = []
            for i in range(m):
                if board[i][j] == 0:
                    continue
                if board[i][j] != curr_candy:
                    if cnt >= 3:
                        mark.append([i - cnt, i])
                        stable = False
                    curr_candy = board[i][j]
                    cnt = 1
                else:
                    cnt += 1
            if cnt >= 3:
                mark.append([m - cnt, m])
                stable = False
            # mark for remove after
            for pair in mark:
                for i in range(pair[0], pair[1]):
                    remove[i][j] = True
        return stable

    def crush(self, board, m, n, remove):
        for i in range(m):
            for j in range(n):
                if remove[i][j]:
                    board[i][j] = 0

    def gravity(self, board, m, n):
        for j in range(n):
            # read/write array tech, bottom up
            write = m - 1
            for i in range(m - 1, -1, -1):
                if board[i][j] != 0:
                    # exchange value instead of rewrite to reduce loop time
                    board[write][j], board[i][j] = board[i][j], board[write][j]
                    write -= 1
            # for i in range(write, -1, -1):
                # board[i][j] = 0