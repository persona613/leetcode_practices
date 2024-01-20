"""
490 ms runtime beats 60.54%
17.08 MB memory beats 59.70%
"""
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def avg(i, j):
            sm = img[i][j]
            cnt = 1
            for d in dirs:
                x = i + d[0]
                y = j + d[1]
                if -1<x<m and -1<y<n:
                    sm += img[x][y]
                    cnt += 1
            return sm // cnt
        m = len(img)
        n = len(img[0])
        res = [[None]*n for _ in range(m)]
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for i in range(m):
            for j in range(n):
                res[i][j] = avg(i, j)
        return res