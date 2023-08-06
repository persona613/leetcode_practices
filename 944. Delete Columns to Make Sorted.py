"""
183 ms runtime beats 27.02%
17.01 MB memory beats 56.75%
"""
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if len(strs) == 1: return 0
        ans = 0
        for i in range(0, len(strs[0])):
            for j in range(1, len(strs)):
                if ord(strs[j][i]) - ord(strs[j-1][i]) < 0:
                    ans += 1
                    break
        return ans