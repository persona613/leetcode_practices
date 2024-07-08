"""
144 ms runtime beats 93.18%
18.66 MB memory beats 97.33%
"""
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # pay rate = wage / quality
        workers = []
        for w, q in zip(wage, quality):
            workers.append((w / q, q))
        workers.sort()

        # take k worker of max pay rate & cost
        mxpr = workers[k - 1][0]
        qtsum = sum(wk[1] for wk in workers[:k])
        cost = mxpr * qtsum
        # max heap of quality
        hp = [-wk[1] for wk in workers[:k]]
        heapify(hp)

        n = len(workers)
        for i in range(k, n):
            # new worker's pay rate, quality
            pr, q = workers[i]
            if q < -hp[0]:
                qtsum += hp[0] + q
                cost = min(cost, pr * qtsum)
                heapq.heappop(hp)
                heapq.heappush(hp, -q)
        return cost