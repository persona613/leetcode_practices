"""
151 ms runtime beats 100%
20.24 MB memory beats 5.17%
"""
class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        k = s[0]
        cnt = 0
        for c in s:
            if c == k:
                cnt += 1
            else:
                if cnt > 2:
                    res.append(k*2)
                else:
                    res.append(k*cnt)
                k = c
                cnt = 1
        if cnt > 2:
            res.append(k*2)
        else:
            res.append(k*cnt)        
        return "".join(res)