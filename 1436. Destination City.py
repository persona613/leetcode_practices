"""
60 ms runtime beats 68.38%
16.33 MB memory beats 45.28%
"""
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        fs = set()
        for p in paths:
            fs.add(p[0])
        for p in paths:
            if p[1] not in fs:
                return p[1]