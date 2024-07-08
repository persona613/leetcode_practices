"""
218 ms runtime beats 82.33%
18.88 MB memory beats 100%
"""
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        gf = [[] for _ in range(n + 1)]
        # in-degree
        inde = [0] * (n + 1)
        for u, v in relations:
            gf[u].append(v)
            inde[v] += 1
        
        q = deque([i for i in range(1, n + 1) if inde[i] == 0])
        ans = 0
        course = []
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                course.append(curr)
                for adj in gf[curr]:
                    inde[adj] -= 1
                    if inde[adj] == 0:
                        q.append(adj)
            ans += 1
        return ans if len(course) == n else -1