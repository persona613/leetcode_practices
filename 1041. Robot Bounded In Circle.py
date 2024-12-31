"""
37 ms runtime beats 42.89%
16.46 MB memory beats 78.36%
"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # N-E-S-W, x-y plane
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dt = 0
        cx = cy = 0
        for i in instructions:
            if i == "G":
                cx += dirs[dt][0]
                cy += dirs[dt][1]
            elif i == "L":
                dt = (dt + 3) % 4
            else:
                dt = (dt + 1) % 4
        if (cx == 0 and cy == 0) or dt != 0:
            return True
        return False