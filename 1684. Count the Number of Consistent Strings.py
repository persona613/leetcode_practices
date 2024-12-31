"""
202 ms runtime beats 78.35%
18.50 MB memory beats 40.73%
"""
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for w in words:
            for c in w:
                if c not in allowed:
                    break
            else:
                ans += 1
        return ans