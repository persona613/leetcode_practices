"""
694 ms runtime beats 15.87%
22.7 MB memory beats 21.62%
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            nonlocal ans
            seen[i].append(j)
            for d in [1, -1]:
                if i+d < 0 or i+d > len(grid)-1:
                    ans += 1
                elif grid[i+d][j] == 0:
                    ans += 1
                else:
                    if j not in seen[i+d]:
                        dfs(i+d, j)
                if j+d < 0 or j+d > len(grid[0])-1:
                    ans += 1
                elif grid[i][j+d] == 0:
                    ans += 1
                else:
                    if j+d not in seen[i]:
                        dfs(i, j+d)               
        ans = 0
        seen = defaultdict(list) # {i: [j]}
        for i in range(len(grid)):
            find = False
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    find = True
                    break
            if find:
                break
        dfs(i, j)
        return ans       