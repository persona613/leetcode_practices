"""
742 ms runtime beats 46.58%
17.05 MB memory beats 8.21%
"""
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # adj matrix[i][j]: whether i knows j
        adj = [[-1] * n for _ in range(n)]
        # one know self
        for i in range(n):
            adj[i][i] = True

        # candidates
        cands = set(range(n))
        for i in range(n):
            if i not in cands:
                continue
            for j in range(n):
                if j not in cands or j == i:
                    continue
                if knows(i, j):
                    adj[i][j] = True
                    cands.remove(i)
                    break
                else:
                    adj[i][j] = False
                    cands.remove(j)
            if len(cands) <= 1:
                break

        if len(cands) == 1:
            curr = cands.pop()
            # check out degree == 1
            for j in range(n):
                if adj[curr][j] == -1:
                    adj[curr][j] = knows(curr, j)
            if sum(adj[curr]) > 1:
                return -1

            # check in degree == n
            indegree = 0
            for i in range(n):
                if adj[i][curr] == -1:
                    adj[i][curr] = knows(i, curr)
                indegree += adj[i][curr]
            if indegree == n:
                return curr
        return -1