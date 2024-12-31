"""
568 ms runtime beats 79.95%
29.74 MB memory beats 90.90%
"""
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sm = sum(chalk)
        remain = k % sm
        for i in range(len(chalk)):
            if remain >= chalk[i]:
                remain -= chalk[i]
            else:
                break
        return i