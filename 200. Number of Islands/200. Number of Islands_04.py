'''
Runtime: 584 ms, faster than 67.71% of Python3 online submissions 
Memory Usage: 16.6 MB, less than 51.29% of Python3 online submissions
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        cnt = 0
        isize = len(grid)
        jsize = len(grid[0])        

        def detect(i, j):
            if grid[i][j] == "0":
                return 
            grid[i][j] = "0"
            
            if j+1 < jsize:
                detect(i, j+1)
            if i+1 < isize:
                detect(i+1, j)
            if j-1 > -1 :
                detect(i, j-1)
            if i-1 > -1:
                detect(i-1, j)
            
            
        for i in range(isize):
            for j in range(jsize):
                if grid[i][j] == "0":
                    continue
                detect(i, j)
                cnt += 1
        return cnt
                            
                        
                    
                