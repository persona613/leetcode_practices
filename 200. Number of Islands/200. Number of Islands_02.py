"""
 Time Limit Exceeded
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        cnt = 0
        detect = []
        # won't clear detect list
        start, tail = -1, -1
        imx = len(grid)
        jmx = len(grid[0])        
        
        for i in range(imx):
            for j in range(jmx):
                if grid[i][j] == "0":
                    continue
                if (i, j) in visited:
                    continue
                    
                detect.append((i, j))
                start += 1
                tail += 1
                
                while start <= tail:
                    t = detect[start]
                    
                    # check right land
                    if t[1]+1 < jmx:
                        right = grid[t[0]][t[1]+1]
                        if not (right == "0" or (t[0],t[1]+1) in visited):
                            detect.append((t[0], t[1]+1))
                            tail += 1
                    # check left land
                    if t[1]-1 > -1:
                        left = grid[t[0]][t[1]-1]
                        if not (left == "0" or (t[0], t[1]-1) in visited):
                            detect.append((t[0], t[1]-1))
                            tail += 1
                    # check down land
                    if t[0]+1 < imx:
                        down = grid[t[0]+1][t[1]]
                        if not (down == "0" or (t[0]+1, t[1]) in visited):
                            detect.append((t[0]+1, t[1]))
                            tail += 1
                    # check up land
                    if t[0]-1 > -1:
                        up = grid[t[0]-1][t[1]]
                        if not (up == "0" or (t[0]-1, t[1]) in visited):
                            detect.append((t[0]-1, t[1]))
                            tail += 1
                    
                    
                    visited.add(t)
                    start += 1
                start -= 1
                cnt += 1
        return cnt
                            
                        
                    
                
