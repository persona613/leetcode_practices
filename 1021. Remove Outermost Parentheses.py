"""
43 ms runtime beats 83.14%
16.5 MB memory beats 15.5%
"""
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt = 0 # (=+1, )=-1
        res = []
        tmp = []
        for p in s:
            tmp.append(p)
            if p == "(":
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    res.extend(tmp[1:-1])
                    tmp = []
        return "".join(res)