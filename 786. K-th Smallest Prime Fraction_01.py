"""
Time Limit Exceeded
56 / 59 testcases passed
"""
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        res = []
        # min heap
        q = []
        # record fraction's two idx
        dic = dict()
        # u = numerator idx
        u = 0
        while len(res) < k and u < n:
            u_val = arr[u]
            # d = demominator idx
            for d in range(u + 1 , n):
                frac = u_val / arr[d]
                q.append(frac)
                dic[frac] = (u_val, arr[d])
            heapq.heapify(q)
            res.append(heapq.heappop(q))
            u += 1
        
        while len(res) < k:
            res.append(heapq.heappop(q))
        return dic[res[-1]]
        