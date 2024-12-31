"""
1015 ms runtime beats 78.00%
54.51 MB memory beats 23.46%
"""
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # max heap
        mxq = []
        for p, c in classes:
            # delta x: ratio change by add one student
            dx = p / c - (p + 1) / (c + 1)
            mxq.append((dx, p, c))
        heapq.heapify(mxq)

        for _ in range(extraStudents):
            # add stedent at max-dx class
            _, p, c = heapq.heappop(mxq)
            p += 1
            c += 1
            dx = p / c - (p + 1) / (c + 1)
            heapq.heappush(mxq, (dx, p, c))
        return sum(p / c for _, p, c in mxq) / len(classes)