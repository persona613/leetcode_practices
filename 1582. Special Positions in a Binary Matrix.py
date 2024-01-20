"""
158 ms runtime beats 49.85%
16.76 MB memory beats 33.33%
"""
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rs = []
        cs = []
        for row in mat:
            rs.append(sum(row))
        for col in zip(*mat):
            cs.append(sum(col))
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1 and rs[i]==1 and cs[j]==1:
                    ans += 1
        return ans