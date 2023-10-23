"""
35 ms runtime beats 91.29%
16.3 MB memory beats 27.68%
"""
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        o = 0 # odd
        for p in position:
            if p % 2 == 1:
                o += 1
        return min(o, len(position)-o)