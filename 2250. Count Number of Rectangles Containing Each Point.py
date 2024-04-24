"""
3410 ms runtime beats 9.69%
38.58 MB memory beats 30.10%
"""
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        n = len(rectangles)
        rectangles.sort()
        # heights array
        hs = [[] for _ in range(101)]
        for rec in rectangles:
            hs[rec[1]].append(rec)
        
        res = []
        for x, y in points:
            cnt = 0
            for h in range(y, 101):
                idx = bisect.bisect_left(hs[h], x, key = lambda r: r[0])
                cnt += len(hs[h]) - idx
            res.append(cnt)
        return res
