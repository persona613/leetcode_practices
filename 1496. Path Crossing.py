"""
32 ms runtime beats 91.90%
17.27 MB memory beats 5.49%
"""
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        moves = {
            "E":(1, 0), "S":(0, -1),
            "W":(-1, 0), "N":(0, 1)
        }
        seen = {(0, 0)}
        x = y = 0
        for p in path:
            dx, dy = moves[p]
            x += dx
            y += dy
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False