"""
396 ms runtime beats 85.16%
17.54 MB memory beats 39.06%
"""
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])
        cnt_by_cols = [0] * n
        cands = []
        for i in range(m):
            # first "B" index each row
            pos = None
            for j in range(n):
                if picture[i][j] == "B":
                    cnt_by_cols[j] += 1
                    if pos is None:
                        pos = j
                    else:
                        pos = -1
            if pos is not None and pos >= 0:
                cands.append(pos)
        ans = 0
        for j in cands:
            if cnt_by_cols[j] == 1:
                ans += 1
        return ans