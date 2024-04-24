"""
588 ms runtime beats 79.87%
27.04 MB memory beats 86.66%
"""
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        lq = costs[:candidates]
        li = candidates
        heapq.heapify(lq)

        rcnt = min(candidates, n - candidates)
        rq = costs[n - rcnt:]
        ri = n - rcnt - 1
        heapq.heapify(rq)

        ans = 0
        take = 0
        while take < k:
            if lq and rq:
                if lq[0] <= rq[0]:
                    ans += heapq.heappop(lq)
                    if li <= ri:
                        heapq.heappush(lq, costs[li])
                        li += 1
                else:
                    ans += heapq.heappop(rq)
                    if li <= ri:
                        heapq.heappush(rq, costs[ri])
                        ri -= 1
            elif lq:
                ans += heapq.heappop(lq)
            else:
                ans += heapq.heappop(rq)
            take += 1
        return ans