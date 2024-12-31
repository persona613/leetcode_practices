"""
19 ms runtime beats 22.52%
18.43 MB memory beats 9.65%
"""
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        teams = set(range(n))
        for e in edges:
            if e[1] in teams:
                teams.remove(e[1])
        return -1 if len(teams) > 1 else teams.pop()