"""
Wrong Answer
22 / 122 testcases passed
Input
height = 5
width = 5
tree = [3,2]
squirrel = [0,1]
nuts =
[[2,0],[4,1],[0,4],[1,3],[1,0],[3,4],[3,0],[2,3],[0,2],[0,0],[2,2],[4,2],[3,3],[4,4],[4,0],[4,3],[3,1],[2,1],[1,4],[2,4]]

Use Testcase
Output
102
Expected
100
"""
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        # tree distance from nuts
        tds = []
        # first min distance nut idx
        idx = 0
        n = len(nuts)
        ans = inf
        # find first nuts idx
        for i in range(n):
            r, c = nuts[i]
            td = abs(tree[0]-r)+abs(tree[1]-c)
            sd = abs(squirrel[0]-r)+abs(squirrel[1]-c)
            if td + sd < ans:
                ans = td + sd
                idx = i
            tds.append(td)
        for i in range(n):
            if i == idx:
                continue
            ans += tds[i] * 2
        return ans
