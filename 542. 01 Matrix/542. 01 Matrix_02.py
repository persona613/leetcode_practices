"""
27 / 50 test cases passed.
Status: Time Limit Exceeded
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[None for _ in range(len(mat[0]))] for _ in range(len(mat))]
        # (i,j)
        zeros = []
        step = float("inf")
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    zeros.append([i, j])
                    res[i][j] = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                step = float("inf")
                for z in zeros:
                    step = min(step, abs(i-z[0])+abs(j-z[1]))
                res[i][j] = step
                
        
        return res

                
            
            
            
