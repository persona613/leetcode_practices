"""
49 / 50 test cases passed.
Status: Time Limit Exceeded
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        
        # find nearest-zero step
        def detect(mat, i, j) -> int:             
            seen = defaultdict(set)
            seen[i].add(j)
            q = deque()
            q.append((i, j))
            step = 0
            while q:
                
                for k in range(len(q)):
                    ci, cj = q.popleft()
                    if mat[ci][cj] == 0:
                        return step
                    
                    for d in {1, -1}:
                        if 0 <= ci+d < len(mat) and cj not in seen[ci+d]:
                            q.append((ci+d, cj))
                            seen[ci+d].add(cj)
                        if 0 <= cj+d < len(mat[0]) and cj+d not in seen[ci]:
                            q.append((ci, cj+d))
                            seen[ci].add(cj+d)                    
                step += 1
            
                
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    continue
                step = detect(mat, i, j)
                res[i][j] = step
        return res

                
            
            
            