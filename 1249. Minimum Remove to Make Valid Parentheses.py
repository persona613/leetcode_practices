"""
66 ms runtime beats 81.73%
18.28 MB memory beats 53.97%
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # open / close parentheses
        opp = clp = 0
        res = []
        for c in s:
            if c == ")":
                if clp + 1 > opp:
                    continue
                else:
                    clp += 1
            elif c == "(":
                opp += 1
            res.append(c)
        if opp == clp:
            return "".join(res)

        for i in range(len(res)-1, -1, -1):
            if res[i] == "(" and opp > clp:
                opp -= 1
                res[i] = ""
                continue
        return "".join(res)