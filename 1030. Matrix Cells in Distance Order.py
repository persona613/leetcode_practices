"""
125 ms runtime beats 91.75%
18.39 MB memory beats 49.03%
"""
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        dic = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                di = abs(r-rCenter) + abs(c-cCenter)
                dic[di].append([r, c])
        res = []
        for k in sorted(dic.keys()):
            res.extend(dic[k])
        return res

        # BFS
        # res = []
        # seen = {(rCenter, cCenter)}
        # q = deque([(rCenter, cCenter)])
        # ds = [1, -1]
        # while q:
        #     for _ in range(len(q)):
        #         r, c = q.popleft()
        #         res.append((r, c))
        #         for d in ds:
        #             tr = r + d
        #             tc = c + d
        #             if -1<tr<rows and (tr,c) not in seen:
        #                 q.append((tr, c))
        #                 seen.add((tr, c))
        #             if -1<tc<cols and (r,tc) not in seen:
        #                 q.append((r, tc))
        #                 seen.add((r, tc))
        # return res