"""
57 ms runtime beats 35.91%
16.4 MB memory beats 47.68%
"""
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res, cnt = [], 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
            elif cnt < 3:
                cnt = 1
            else:
                res.append([i-cnt, i-1])
                cnt = 1
        if cnt >= 3:
            res.append([i+1-cnt, i])
        return res