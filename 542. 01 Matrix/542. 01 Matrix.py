"""
Runtime: 1875 ms, faster than 35.95% of Python3 online submissions 
Memory Usage: 17.2 MB, less than 52.80% of Python3 online submissions
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # find nearest-zero step
        def detect(mat, i, j) -> int:             
            seen = defaultdict(set)
            seen[i].add(j)
            q = deque([(i, j)])
            
            step = 0
            while q:
                
                for k in range(len(q)):
                    ci, cj = q.popleft()
                    if mat[ci][cj] == 0:
                        return ci, cj, step
                    
                    for d in {1, -1}:
                        if 0 <= ci+d < len(mat) and cj not in seen[ci+d]:
                            q.append((ci+d, cj))
                            seen[ci+d].add(cj)
                        if 0 <= cj+d < len(mat[0]) and cj+d not in seen[ci]:
                            q.append((ci, cj+d))
                            seen[ci].add(cj+d)                    
                step += 1
                
        # fill steps between zero(zi,zj) and cell(i,j)
        def fillstep(mat, i, j, zi, zj, step):
            isize = abs(i-zi)+1
            jsize = abs(j-zj)+1
            if i <= zi and j <= zj:
                for r in range(isize):
                    for c in range(jsize):
                        mat[i+r][j+c] = abs(i+r-zi)+abs(j+c-zj)
            elif i <= zi and j > zj:
                for r in range(isize):
                    for c in range(jsize):
                        mat[i+r][j-c] = abs(i+r-zi)+abs(j-c-zj)
            elif i > zi and j <= zj:
                for r in range(isize):
                    for c in range(jsize):
                        mat[i-r][j+c] = abs(i-r-zi)+abs(j+c-zj)
            elif i > zi and j > zj:
                for r in range(isize):
                    for c in range(jsize):
                        mat[i-r][j-c] = abs(i-r-zi)+abs(j-c-zj)            
            return mat
                
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 1:
                    continue                
                zi, zj, step = detect(mat, i, j)
                if step == 1:
                    continue
                mat = fillstep(mat, i, j, zi, zj, step)
        return mat

                
