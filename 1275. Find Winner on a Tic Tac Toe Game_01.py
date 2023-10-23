"""
Wrong Answer
80 / 100 testcases passed
Editorial
Input
moves =
[[0,2],[1,0],[2,2],[1,2],[2,0],[0,0],[0,1],[2,1],[1,1]]

Use Testcase
Output
"Draw"
Expected
"A"
"""
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) == 9: return "Draw"
        if len(moves) <= 4: return "Pending"

        gd = [[0]*3 for _ in range(3)]
        for i in range(len(moves)):
            r, c = moves[i]
            if i % 2 == 0:
                gd[r][c] = -1
            else:
                gd[r][c] = 1
        for row in gd:
            sm = sum(row)
            if sm == -3: return "A"
            if sm == 3: return "B"
        for col in zip(*gd):
            sm = sum(col)
            if sm == -3: return "A"
            if sm == 3: return "B"

        sm = sum(gd[i][i] for i in range(3))
        if sm == -3: return "A"
        if sm == 3: return "B"
        sm = sum(gd[i][2-i] for i in range(3))
        if sm == -3: return "A"
        if sm == 3: return "B"
        return "Pending"


        # # count = gd[row(0,2),col(3,5),dia(6,7)]
        # gd = [0]*8
        # for i in range(len(moves)):
        #     r, c = moves[i]
        #     if i % 2 == 0: d = -1
        #     else: d = 1
        #     gd[r] += d
        #     gd[3+c] += d
        #     if r == c:
        #         gd[6] += d
        #     if r + c == 2:
        #         gd[7] += d
        # for g in gd:
        #     if g == -3:
        #         return "A"
        #     elif g == 3:
        #         return "B"
        # return "Pending"