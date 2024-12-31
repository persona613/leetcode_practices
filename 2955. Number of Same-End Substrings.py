"""
2388 ms runtime beats 5.63%
45.52 MB memory beats 47.66%
"""
class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # 26 characters count map, column: one-index
        count = [[0] * (n + 1) for _ in range(26)]
        for i, c in enumerate(s):
            count[ord(c) - ord("a")][i + 1] += 1
        # build presum of 26 characters
        for i in range(26):
            for j in range(1, n + 1):
                count[i][j] += count[i][j - 1]
        
        res = []
        for l, r in queries:
            # count of curr string's same-end substrings
            curr = 0
            # calculate each characters's count
            for i in range(26):
                k = count[i][r + 1] - count[i][l]
                curr += k * (k + 1) // 2
            res.append(curr)
        return res