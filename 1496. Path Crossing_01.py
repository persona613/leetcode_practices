"""
47 ms runtime beats 9.10%
16.46 MB memory beats 21.84%
"""
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        pts = {(0, 0)}
        for p in path:
            if p == "N":
                y += 1
            elif p == "S":
                y -= 1
            elif p == "E":
                x += 1
            else:
                x -= 1
            if (x, y) in pts:
                return True
            pts.add((x, y))
        return False