"""
125 ms runtime beats 95.49%
17.50 MB memory beats 9.64%
"""
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        # distance(tree, nuts)
        dt = []
        x, y = tree
        p, q = squirrel
        for nu in nuts:
            dt.append(abs(x - nu[0]) + abs(y - nu[1]))
        # distance(squirrel, nuts)
        ds = []
        for nu in nuts:
            ds.append(abs(p - nu[0]) + abs(q - nu[1]))
        # save max distance = max(dt - ds)
        save = -inf
        for i in range(len(nuts)):
            d = dt[i] - ds[i]
            if d > save:
                save = d
        return sum(t*2 for t in dt) - save
