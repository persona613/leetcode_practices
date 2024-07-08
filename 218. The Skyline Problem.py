"""
100 ms runtime beats 73.67%
22.52 MB memory beats 22.24%
"""
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for l, r, h in buildings:
            points.append((-h, l, r))
            points.append((h, r, -1)) # end point
        points.sort(key = lambda x: (x[1], x[0]))
        # max heap for heights, origin h = 0
        q = [(0, 0, inf)]
        pre = []
        for ch, cx, cr in points:
            # start point
            if ch < 0:
                # curr height > maintain height
                if ch < q[0][0]:
                    pre.append((cx, -ch))
                heapq.heappush(q, (ch, cx, cr))
            # end point
            else:
                # remove pass over building
                while q[0][2] <= cx:
                    heapq.heappop(q)
                # compare maintain height with pre[-1]'s height
                # if new height < pre height
                if -q[0][0] < pre[-1][1]:
                    pre.append((cx, -q[0][0]))
        return pre