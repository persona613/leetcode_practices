"""
792 ms runtime beats 74.22%
112.60 MB memory beats 89.38%
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)
        m = len(bikes)
        # dic = {distance:[(Wi, Bi),...]}
        dic = defaultdict(list)
        # workers' bike idx, cnt of workers had bike
        wks = [None]*n
        wcnt = 0
        # bikes used state
        bks = [None]*m

        for i in range(n):
            x, y = workers[i]
            for j in range(m):
                d = abs(x-bikes[j][0]) + abs(y-bikes[j][1])
                dic[d].append((i, j))
        
        # max distance = 1998
        for d in range(1, 1999):
            arr = dic[d]
            for wi, bi in arr:
                if wks[wi] == None and bks[bi] == None:
                    wks[wi] = bi
                    bks[bi] = 1
                    wcnt += 1
                if wcnt == n:
                    break
        return wks

