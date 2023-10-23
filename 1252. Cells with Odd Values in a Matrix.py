"""
41 ms runtime beats 96.40%
16.3 MB memory beats 62.54%
"""
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rf = [0]*m # row frequency
        cf = [0]*n
        for r, c in indices:
            rf[r] ^= 1
            cf[c] ^= 1
            # rf[r] = (rf[r]+1) % 2
            # cf[c] = (cf[c]+1) % 2
        rod = rf.count(1)
        cod = cf.count(1)
        return rod*(n-cod) + cod*(m-rod)