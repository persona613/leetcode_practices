"""
494 ms runtime beats 24.77%
17.60 MB memory beats 5.67%
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = dict()
        for a in tasks:
            d[a] = d.get(a, 0) + 1
        q = []
        for k, v in d.items():
            q.append((-v, k)) # 1=ocurrance time
        heapq.heapify(q)

        # preidx = {(task, pre_idx)}
        preidx = dict()
        for k in d:
            preidx[k] = - n - 1
        res = []
        while q:
            tmp = []
            for _ in range(n + 1):
                if q:
                    cnt, task = heapq.heappop(q)
                    if len(res) > preidx[task] + n:
                        preidx[task] = len(res)
                        res.append(task)
                        if -cnt > 1:
                            tmp.append((cnt + 1, task))
                    else:
                        res.append("IDLE")
                        tmp.append((cnt, task))
                else:
                    if tmp:
                        res.append("IDLE")
                    else:
                        break
            while tmp:
                heapq.heappush(q, tmp.pop())
        # print(res)
        return len(res)