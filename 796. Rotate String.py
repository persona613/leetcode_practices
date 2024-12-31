"""
0 ms runtime beats 100.00%
16.54 MB memory beats 40.35%
"""
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) <= len(goal) and goal in s + s