"""
43 ms runtime beats 74.39%
16.56 MB memory beats 78.35%
"""
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def backtrack(i, t, path):
            if i == n:
                self.ans = "".join(path)
                t -= 1
                return t
            
            for c in chars:
                if path and path[-1] == c:
                    continue
                path.append(c)
                # recursive update variable
                t = backtrack(i + 1, t, path)
                if t == 0:
                    return 0
                path.pop()
            return t

        if k > 3 * 2 ** (n - 1):
            return ""
        chars = "abc"
        self.ans = ""
        backtrack(0, k, [])
        return self.ans