"""
643 ms runtime beats 67.16%
32.38 MB memory beats 98.04%
"""
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        n = len(routes)
        # bus routes set
        brs = []
        for r in routes:
            brs.append(set(r))
        # bus connect edges
        bse = [[] for _ in range(n)]
        for i in range(n):
            a = brs[i]
            for j in range(i+1, n):
                b = brs[j]
                # check connect
                if len(a) <= len(b):
                    ct = a.isdisjoint(b)
                else:
                    ct = b.isdisjoint(a)
                if not ct:
                    bse[i].append(j)
                    bse[j].append(i)
        # bus contain end stop
        ed_bus = []
        for i in range(n):
            if target in brs[i]:
                ed_bus.append(i)
        # bus contain start stop
        st_bus = set()
        for i in range(n):
            if source in brs[i]:
                st_bus.add(i)
                        
        def bfs(bus, st_bus, bse):
            cnt = 1
            if bus in st_bus:
                return cnt
            q = deque([bus])
            seen = {bus}
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    # take next bus
                    for nb in bse[curr]:
                        if nb not in seen:
                            if nb in st_bus:
                                return cnt+1
                            q.append(nb)
                            seen.add(nb)
                cnt += 1
            return 0        
        ans = n+1
        for b in ed_bus:
            ret = bfs(b, st_bus, bse)
            if ret:
                ans = min(ans, ret)
        return -1 if ans==n+1 else ans            
