"""
61 ms runtime beats 16.21%
16.35 MB memory beats 83.01%
"""
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for lo in logs:
            if lo[0].isalnum():
                ans += 1
            elif lo == "../" and ans > 0:
                ans -= 1
        return ans