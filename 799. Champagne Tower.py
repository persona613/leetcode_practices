"""
93 ms runtime beats 49.51%
17.2 MB memory beats 5.39%
"""
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        def gl(poured,i,j):
            if i<0 or j<0 or j>i:
                return 0
            if dp[i][j] != None:
                return dp[i][j]
            if i==0 and j==0:
                dp[i][j] = poured
                return poured
            dp[i][j] = max((gl(poured,i-1,j-1)-1)/2,0) \
                     + max((gl(poured,i-1,j)-1)/2,0)
            return dp[i][j]
        
        dp = [[None]*(i+1) for i in range(query_row+1)]
        ans = gl(poured, query_row, query_glass)
        return min(1, ans)