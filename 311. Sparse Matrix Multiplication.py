"""
54 ms runtime beats 71.54%
16.83 MB memory beats 49.26%
"""
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        def product(dic1, dic2):
            ans = 0
            for key in dic1:
                if key in dic2:
                    ans += dic1[key] * dic2[key]
            return ans

        # [m, k] * [k, n] = [m, n]
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])
        
        # sparse matrix 1, {row: {col: value}}
        spm1 = defaultdict(dict)
        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:
                    spm1[i][j] = mat1[i][j]

        # sparse matrix 1, {col: {row: value}}
        spm2 = defaultdict(dict)
        for j in range(n):
            for i in range(k):
                if mat2[i][j] != 0:
                    spm2[j][i] = mat2[i][j]
        
        res = [[None] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = product(spm1[i], spm2[j])
        return res