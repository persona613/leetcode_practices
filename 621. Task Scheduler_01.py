"""
Wrong Answer
70 / 71 testcases passed

Editorial
Input
tasks =
["F","J","J","A","J","F","C","H","J","B","E","G","G","F","A","C","I","F","J","C","J","C","H","C","A","D","G","H","B","F","G","C","C","A","E","B","H","J","E","I","F","D","E","A","C","D","B","D","J","J","C","F","D","D","J","H","A","E","C","D","J","D","G","G","B","C","E","G","H","I","D","H","F","E","I","B","D","E","I","E","C","J","G","I","D","E","D","J","C","A","C","C","D","I","J","B","D","H","H","J","G","B","G","A","H","E","H","E","D","E","J","E","J","C","F","C","J","G","B","C","I","I","H","F","A","D","G","F","C","C","F","G","C","J","B","B","I","C","J","J","E","G","H","C","I","G","J","I","G","G","J","G","G","E","G","B","I","J","B","H","D","H","G","F","C","H","C","D","A","G","B","H","H","B","J","C","A","F","J","G","F","E","B","F","E","B","B","A","E","F","E","H","I","I","C","G","J","D","H","E","F","G","G","D","E","B","F","J","J","J","D","H","E","B","D","J","I","F","C","I","E","H","F","E","G","D","E","C","F","E","D","E","A","I","E","A","D","H","G","C","I","E","G","A","H","I","G","G","A","G"...
n =
8

Use Testcase
Output
1025
Expected
1000
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = dict()
        for a in tasks:
            d[a] = d.get(a, 0) + 1
        q = []
        for k, v in d.items():
            q.append((1, -v, k)) # 1=ocurrance time
        heapq.heapify(q)

        # preidx = {(task, pre_idx)}
        preidx = dict()
        for k in d:
            preidx[k] = - n - 1
        res = []
        ocr_head, cnt_head, head = heapq.heappop(q)
        for i in range(-cnt_head - 1): # intervals = highest freq - 1
            res.append(head)
            # IDLE slots = n
            for j in range(n):
                if q:
                    ocr, cnt, task = heapq.heappop(q)
                    if len(res) > preidx[task] + n:
                        preidx[task] = len(res)
                        res.append(task)
                        if -cnt > 1:
                            heapq.heappush(q, (ocr + 1, cnt + 1, task))
                    else:
                        res.append("IDLE")
                        heapq.heappush(q, (ocr, cnt, task))
                else:
                    res.append("IDLE")
        res.append(head)
        while q:
            ocr, cnt, task = heapq.heappop(q)
            res.append(task)
            if -cnt > 1:
                heapq.heappush(q, (ocr + 1, cnt + 1, task))
        # print(res)
        return len(res)