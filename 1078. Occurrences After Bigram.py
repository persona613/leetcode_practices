"""
36 ms runtime beats 85.4%
16.3 MB memory beats 70.96%
"""
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ts = text.split()
        res = []
        f1 = 0
        for i in range(len(ts)-1):
            if f1:
                if ts[i] == second:
                    res.append(ts[i+1])
                f1 = 0
            if ts[i] == first:
                f1 = 1
        return res