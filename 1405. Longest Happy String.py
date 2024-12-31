"""
39 ms runtime beats 26.91%
16.61 MB memory beats 29.54%
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        # take k of char from pair
        def take(pair, k):
            if pair[0] <= -k:
                pair[0] += k
                res.append(pair[1] * k)
            else:
                pair[0] += 1
                res.append(pair[1])
            if pair[0] < 0:
                heapq.heappush(q, pair)

        # max heap
        q = []
        for p in [[-a, "a"], [-b, "b"], [-c, "c"]]:
            if p[0] < 0:
                q.append(p)
        heapq.heapify(q)

        res = []
        while len(q) > 1:
            p1 = heapq.heappop(q)
            p2 = heapq.heappop(q)
            if p1[0] == p2[0]:
                # avoid 3 same char
                if res and p1[1] == res[-1][-1]:
                    p1, p2 = p2, p1
                take(p1, 2)
                take(p2, 2)
            else:
                take(p1, 2)
                take(p2, 1)
        if q:
            take(heapq.heappop(q), 2)
        return "".join(res)