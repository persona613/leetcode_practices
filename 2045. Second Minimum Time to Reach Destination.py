"""
17.40 ms runtime beats 89.40%
26.31 MB memory beats 78.81%
"""
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adjs = [[] for _ in range(n + 1)]
        for u, v in edges:
            adjs[u].append(v)
            adjs[v].append(u)

        # record arrive time of every node at most 2 arriving
        arr = [[] for _ in range(n + 1)]
        q = deque([1])
        curr_cost = 0
        while q:

            for _ in range(len(q)):
                curr = q.popleft()
                # first or second arrive curr node with diff cost_time
                if len(arr[curr]) > 1:
                    continue
                if not arr[curr] or arr[curr][-1] != curr_cost:
                    arr[curr].append(curr_cost)

                    for adj in adjs[curr]:
                        q.append(adj)

            if len(arr[n]) > 1:
                return arr[n][-1]

            # pre calculate arrive next-node time
            # intervals = cost // change, if intervals is odd = red light
            if (curr_cost // change) % 2:
                # +wait time till next interval
                curr_cost += change - (curr_cost % change)

            # +time for arrive next node
            curr_cost += time