"""
90 ms runtime beats 54.00%
18.18 MB memory beats 91.14%
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        gf = defaultdict(set)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            gf[v].add(u)
            indegree[u] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        while q:
            curr = q.popleft()
            order.append(curr)
            for adj in gf[curr]:
                indegree[adj] -= 1

                if indegree[adj] == 0:
                    q.append(adj)
        return True if len(order) == numCourses else False