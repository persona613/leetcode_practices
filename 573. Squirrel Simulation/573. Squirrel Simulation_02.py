"""
Wrong Answer
97 / 122 testcases passed
Editorial
Input
height = 4
width = 8
tree = [1,5]
squirrel = [2,7]
nuts =
[[0,0],[0,7],[1,7],[2,1],[3,2],[2,6],[0,4],[2,4],[2,3],[3,0],[1,0],[0,1]]

Use Testcase
Output
95
Expected
93
"""
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        # distance(tree, nuts)
        dt = []
        x, y = tree
        p, q = squirrel
        for nu in nuts:
            dt.append(abs(x - nu[0]) + abs(y - nu[1]))
        mx = max(dt)
        # distance(squirrel, nuts) where dt max
        ds = []
        for i in range(len(nuts)):
            if dt[i] == mx:
                d = abs(p-nuts[i][0]) + abs(q - nuts[i][1])
                ds.append(d)
        mi = min(ds)
        # save max distance = max(dt) - min(ds)
        return sum(t*2 for t in dt) - (mx - mi)
