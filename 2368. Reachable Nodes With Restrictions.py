"""
1227 ms runtime beats 94.38%
74.69 MB memory beats 91.24%
"""
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        rst = set(restricted)
        seen = {0}
        cnt = 0

        stk = [0]
        while stk:
            curr = stk.pop()
            cnt += 1
            for adj in g[curr]:
                if adj not in seen and adj not in rst:
                    seen.add(adj)
                    stk.append(adj)
        return cnt
