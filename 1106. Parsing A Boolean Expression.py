"""
11 ms runtime beats 100.00%
16.66 MB memory beats 80.84%
"""
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # import operator
        i = 0
        n = len(expression)
        # operator stack
        optr = []
        # operands stack
        opds = []
        while i < n:
            curr = expression[i]
            if curr == "!":
                optr.append(operator.not_)
            elif curr == "&":
                optr.append(operator.and_)
            elif curr == "|":
                optr.append(operator.or_)
            elif curr == "(":
                opds.append(-1)
            elif curr == "t":
                opds.append(True)
            elif curr == "f":
                opds.append(False)
            elif curr == ")":
                opt = optr.pop()
                boo = opds.pop()
                if opt == operator.not_:
                    boo = not boo
                else:
                    while opds[-1] != -1:
                        boo = opt(boo, opds.pop())
                opds.pop()
                opds.append(boo)
            i += 1
        return opds.pop()