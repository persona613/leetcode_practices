"""
44 ms runtime beats 7.6%
16.3 MB memory beats 9.55%
"""
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())