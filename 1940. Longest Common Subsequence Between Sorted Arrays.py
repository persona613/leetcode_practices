"""
196 ms runtime beats 87.18%
16.97 MB memory beats 76.92%
"""
class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        n = len(arrays)
        cnt = [0] * 101
        for arr in arrays:
            for a in arr:
                cnt[a] += 1
        res = []
        for i in range(101):
            if cnt[i] == n:
                res.append(i)
        return res