"""
99 ms runtime beats 87.10%
17.58 MB memory beats 55.09%
"""
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        print(n)
        j = 0
        for i in range(n):
            if start[i] == "_":
                continue

            while j < n and target[j] == "_":
                j += 1
            if j >= n:
                return False
            
            if start[i] != target[j]:
                return False
            if start[i] == "L" and i < j:
                return False
            if start[i] == "R" and i > j:
                return False

            j += 1

        while j < n and target[j] == "_":
            j += 1
        return j >= n