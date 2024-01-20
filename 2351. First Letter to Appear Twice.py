"""
38 ms runtime beats 51.36%
16.21 MB memory beats 39.11%
"""
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)