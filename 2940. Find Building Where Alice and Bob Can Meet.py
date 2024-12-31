"""
665 ms runtime beats 39.18%
37.58 MB memory beats 84.58%
"""
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # reorder queries's (x, y)
        newq = []
        for pair in queries:
            if pair[0] > pair[1]:
                newq.append((pair[1], pair[0]))
            else:
                newq.append(pair[:])
        # sort by y-increasing
        qidx = sorted(range(len(newq)), key = lambda x: newq[x][1])

        # decreasing monotonic stack backward
        hi = len(heights) - 1
        stk = deque()
        # search by y-decreasing
        res = [None] * len(queries)
        while qidx:
            cq = qidx.pop()
            cx, cy = newq[cq]

            # maintain heights mono-stack after y
            while hi > cy:
                while stk and heights[stk[0]] < heights[hi]:
                    stk.popleft()
                stk.appendleft(hi)
                hi -= 1
            
            if cx == cy or heights[cx] < heights[cy]:
                res[cq] = cy
            # find element after cy > heights[cx]
            else:
                t = bisect.bisect_right(stk, heights[cx], key = lambda x: heights[x])
                res[cq] = stk[t] if t < len(stk) else -1
        return res