"""
38 ms runtime beats 73.33%
14.3 MB memory beats 36.61%
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        tmp = ""
        pl = 0
        pr = 0
        qe = deque([[tmp, pl, pr]])
        i = 0
        while i < 2*n:
            for _ in range(len(qe)):
                tmp, pl, pr = qe.popleft()
                for c in ["(", ")"]:
                    if c == "(":
                        if pl < n:
                            qe.append([tmp+c, pl+1, pr+1])
                    else:
                        if pr > 0:
                            qe.append([tmp+c, pl, pr-1])
            i += 1
        for ls in qe:
            res.append(ls[0])
        return res
            
        