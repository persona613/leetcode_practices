"""
47 ms runtime beats 72.62%
16.80 MB memory beats 36.19%
"""
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for lo in logs:
            if lo == "../":
                if level > 0:
                    level -= 1
            elif lo != "./":
                level += 1
        return level