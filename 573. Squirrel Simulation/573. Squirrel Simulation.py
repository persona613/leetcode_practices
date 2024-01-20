"""
132 ms runtime beats 77.44%
17.48 MB memory beats 29.19%
"""
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        # distance(tree, nuts)
        x, y = tree
        p, q = squirrel
        save = -inf
        total = 0
        for r, c in nuts:
            dt = abs(x - r) + abs(y - c)
            ds = abs(p - r) + abs(q - c)
            # save max distance = max(dt - ds)
            d = dt - ds
            if d > save:
                save = d
            total += dt * 2
        return  total - save
