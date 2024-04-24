"""
475 ms runtime beats 40.24%
35.14 MB memory beats 65.97%
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def backtrack(i, curr, path):
            if i == n:
                res.append(path[:])
                return

            curr.append(s[i])
            if pal(curr):
                path.append("".join(curr))
                backtrack(i + 1, [], path)
                path.pop()

            if i == n - 1:
                return
            backtrack(i + 1, curr, path)

        def pal(arr):
            return arr == arr[::-1]

        n = len(s)
        res = []
        backtrack(0, [], [])
        return res