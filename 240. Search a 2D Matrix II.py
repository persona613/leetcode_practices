"""
170 ms runtime beats 93.45%
20.5 MB memory beats 11.70%
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        # left-top corner, right-bottom corner = [i,j]
        def find_upboun(p,q,m,n):
            j = (n+q) // 2
            i = p
            while i <= m:
                if matrix[i][j] < target:
                    i += 1
                else:
                    return [i, j]
                    # up-boundary, includ
            return [i, j]
        
        def search_smat(smat):
            nonlocal matrix
            p, q = smat[0][0], smat[0][1]
            m, n = smat[1][0], smat[1][1]
            i, j = find_upboun(p,q,m,n)
            # print("upboun:",[i,j])
            if i <= m and matrix[i][j] == target:
                return True
            
            if i <= m and j-1 >= q:
                smat1 = [[i,q],[m,j-1]]
                # print("smat1:",smat1)
                if search_smat(smat1):
                    return True
            if i-1 >= p and j+1 <= n:
                smat2 = [[p,j+1],[i-1,n]]
                # print("smat2:",smat2)
                if search_smat(smat2):
                    return True
            return False
        
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        smat = [[0,0], [m,n]]
        return search_smat(smat)

        