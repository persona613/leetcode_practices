"""
61 ms runtime beats 62.26%
16.40 MB memory beats 29.68%
"""
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mp = dict()
        for a, b in paths:
            mp[a] = b
        while a in mp:
            a = mp[a]
        return a