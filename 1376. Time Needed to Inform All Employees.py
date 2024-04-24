"""
890 ms runtime beats 90.92%
47.44 MB memory beats 51.46%
"""
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(set)
        for i, v in enumerate(manager):
            g[v].add(i)
        ans = 0
        q = deque([(headID, 0)])
        while q:
            curr, time = q.popleft()
            info = informTime[curr]
            if info:
                for ni in g[curr]:
                    q.append((ni, time + info))
            else:
                if time > ans:
                    ans = time
        return ans