"""
1367 ms runtime beats 99.41%
84 MB memory beats 19.41%
"""
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # dag{nextcourse:[precourse]}
        g = {i:[] for i in range(1, n+1)}
        for pr, nt in relations:
            g[nt].append(pr)            
        # dp[i]= (i+1)course completed total time
        dp = [None]*(n+1)
        for i in range(1, n+1):
            if dp[i] == None:
                self.dfs(g, dp, i, time)
        return max(dp[1:])

    def dfs(self, g, dp, nt, time):
        if dp[nt] != None:
            return dp[nt]
        if not g[nt]:
            dp[nt] = time[nt-1]
            return dp[nt]
        mx = 0
        for pr in g[nt]:
            if dp[pr] != None:
                t = dp[pr]
            else:
                t = self.dfs(g, dp, pr, time)
            if t > mx:
                mx = t
        dp[nt] = mx + time[nt-1]
        return dp[nt]