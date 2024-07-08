"""
469 ms runtime beats 49.08%
34.52 MB memory beats 79.09%
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def pal(word):
            return word == word[::-1]

        def backtrack(i, path):
            if i == n:
                res.append(path[:])
                return
            
            # cut string to each j
            for j in range(i + 1, n + 1):
                curr = s[i: j]
                if pal(curr):
                    path.append(curr)
                    backtrack(j, path)
                    path.pop()

        n = len(s)
        res = []
        backtrack(0, [])
        return res