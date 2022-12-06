'''
Runtime: 1141 ms, faster than 10.79% of Python3 online submissions 
Memory Usage: 19.9 MB, less than 38.54% of Python3 online submissions
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = defaultdict(list) # key is i-index, value is j-index
        cnt = 0
        detect = []
        # won't clear detect list
        start, tail = -1, -1
        imx = len(grid)
        jmx = len(grid[0])        
        
        for i in range(imx):
            for j in range(jmx):
                if j in visit[i]:
                    continue
                if grid[i][j] == "0":
                    visit[i].append(j)
                    continue

                detect.append((i, j))
                visit[i].append(j)
                start += 1
                tail += 1
                
                while start <= tail:
                    it = detect[start][0]
                    jt = detect[start][1]
                
                    # check right
                    if jt+1 < jmx:
                        if jt+1 not in visit[it]:
                            visit[it].append(jt+1)
                            if grid[it][jt+1] == "1":
                                detect.append((it, jt+1))
                                tail += 1
                    # check left
                    if jt-1 > -1:
                        if jt-1 not in visit[it]:
                            visit[it].append(jt-1)
                            if grid[it][jt-1] == "1":
                                detect.append((it, jt-1))
                                tail += 1                                
                    # check down
                    if it+1 < imx:
                        if jt not in visit[it+1]:
                            visit[it+1].append(jt)
                            if grid[it+1][jt] == "1":
                                detect.append((it+1, jt))
                                tail += 1
                    # check up
                    if it-1 > -1:
                        if jt not in visit[it-1]:
                            visit[it-1].append(jt)
                            if grid[it-1][jt] == "1":
                                detect.append((it-1, jt))
                                tail += 1
                    start += 1
                start -= 1
                cnt += 1
        return cnt
                            
                        
                    
                                    
                        
                    
                
