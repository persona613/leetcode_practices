"""
1190 ms runtime beats 18.30%
308.75 MB memory beats 14.10%
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == 0 or j == 0:
                memo[(i, j)] = 0
                return 0

            if text1[i-1] == text2[j-1]:
                memo[(i, j)] = dfs(i-1, j-1) + 1
            else:
                memo[(i, j)] = max(dfs(i-1, j), dfs(i, j-1))
            return memo[(i, j)]

        memo = {}
        return dfs(len(text1), len(text2))
