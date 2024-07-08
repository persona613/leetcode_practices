"""
Runtime Error
26 / 180 testcases passed
submitted at Jun 22, 2024 15:53

Editorial
KeyError: 1
    cands.remove(i)
Line 21 in findCelebrity (Solution.py)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ret = Solution().findCelebrity(n)
Line 65 in __helper__ (Solution.py)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    celebrity = __DriverSolution__().__helper__(matrix)
Line 81 in _driver (Solution.py)
    _driver()
Line 91 in <module> (Solution.py)
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