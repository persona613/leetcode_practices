"""
412 ms runtime beats 98.46%
21.85 MB memory beats 10%
"""
class Solution:
    def robotWithString(self, s: str) -> str:
        p = []
        t = []
        n = len(s)
        mi = [None] * n
        mi[-1] = s[-1]
        for i in range(n-2, -1, -1):
            mi[i] = min(s[i], mi[i+1])
        i = 0
        while i < n:
            while t and t[-1] <= mi[i]:
                p.append(t.pop())
            t.append(s[i])
            i += 1
        if t:
            p.extend(t[::-1])
        
        return "".join(p)

        
