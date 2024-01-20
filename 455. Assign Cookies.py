"""
286 ms runtime beats 9.56%
19.17 MB memory beats 13.41%
"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = j = 0
        n = len(g)
        m = len(s)
        g.sort()
        s.sort()
        while i < n and j < m:
            if s[j] >= g[i]:
                j += 1
                i += 1
            else:
                j += 1
        return i