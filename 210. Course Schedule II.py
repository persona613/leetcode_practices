"""
81 ms runtime beats 94.75%
18.22 MB memory beats 84.06%
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # try kahn's algorithm
        gf = [[] for _ in range(numCourses)]
        indgree = [0] * numCourses
        for v, u in prerequisites:
            gf[u].append(v)
            indgree[v] += 1
        
        q = deque([i for i in range(numCourses) if indgree[i] == 0])
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for adj in gf[curr]:
                indgree[adj] -= 1
                if indgree[adj] == 0:
                    q.append(adj)
        return res if len(res) == numCourses else []
        