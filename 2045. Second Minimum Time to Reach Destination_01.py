"""
Time Limit Exceeded
51 / 76 testcases passed
Last Executed Input
Use Testcase
n =
10000
"""
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adjs = [[] for _ in range(n + 1)]
        for u, v in edges:
            adjs[u].append(v)
            adjs[v].append(u)

        res = []
        # (curr node, pre node, cost time)
        q = deque([(1, -1, 0)])
        while q:
            curr, pre, cost = q.popleft()
            if curr == n:
                if res and res[-1] != cost:
                    return cost
                res.append(cost)

            # intervals = cost // change, if odd = red light
            if (cost // change) % 2:
                # wait till next interval
                cost += change - (cost % change)
            
            # +time for arrive next node
            cost += time
            for adj in adjs[curr]:
                if adj == pre:
                    continue
                q.append((adj, curr, cost))

        # if only one path, add two more edges time
        cost = res[0]
        for _ in range(2):
            if (cost // change) % 2:
                cost += change - (cost % change)
            cost += time
        return cost