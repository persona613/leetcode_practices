"""
86 ms runtime beats 17.30%
16.5 MB memory beats 21.94%
"""
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) % 2 != 0:
            return False
        # position(x, y)
        pos = [0, 0] 
        for m in moves:
            if m == 'R':
                pos[0] += 1
            elif m == 'L':
                pos[0] -= 1
            elif m == 'U':
                pos[1] += 1
            elif m == 'D':
                pos[1] -= 1
        return pos == [0, 0]