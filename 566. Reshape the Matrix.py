"""
111 ms runtime beats 10.93%
17.1 MB memory beats 17.25%
"""
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        if len(mat) == r and len(mat[0]) == c:
            return mat
        res = [[] for _ in range(r)]
        k = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(res[k]) == c:
                    k += 1
                res[k].append(mat[i][j])
        return res