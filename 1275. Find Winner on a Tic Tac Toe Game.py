"""
24 ms runtime beats 99.68%
16.11 MB memory beats 96.93%
"""
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = len(moves)
        if n <= 4: return "Pending"
        # count = gd[row(0,2),col(3,5),dia(6,7)]
        gd = [0]*8
        for i in range(n):
            r, c = moves[i]
            d = 4**(i%2) # A=1,B=4
            gd[r] += d
            gd[3+c] += d
            if r == c:
                gd[6] += d
            if r + c == 2:
                gd[7] += d
        for g in gd:
            if g == 3:
                return "A"
            elif g == 12:
                return "B"
        return "Pending" if n<9 else "Draw"


        # gd = [[0]*3 for _ in range(3)]
        # n = len(moves)
        # for i in range(n):
        #     r, c = moves[i]
        #     if i % 2 == 0:
        #         gd[r][c] = -1
        #     else:
        #         gd[r][c] = 1
        # for row in gd:
        #     sm = sum(row)
        #     if sm == -3: return "A"
        #     if sm == 3: return "B"
        # for col in zip(*gd):
        #     sm = sum(col)
        #     if sm == -3: return "A"
        #     if sm == 3: return "B"

        # sm = sum(gd[i][i] for i in range(3))
        # if sm == -3: return "A"
        # if sm == 3: return "B"
        # sm = sum(gd[i][2-i] for i in range(3))
        # if sm == -3: return "A"
        # if sm == 3: return "B"
        # return "Pending" if n<9 else "Draw"