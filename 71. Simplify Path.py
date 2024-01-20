"""
79 ms runtime beats 5.96%
17.42 MB memory beats 7.58%
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        dots = 0
        for p in path:
            if p == ".":
                dots += 1
            else:
                if dots == 1 and stk[-2] == "/" and p =="/":
                    stk.pop()
                elif dots == 2 and stk[-3] == "/" and p == "/":
                    for _ in range(3):
                        stk.pop()
                    while stk and stk[-1] != "/":
                        stk.pop()
                dots = 0
                if stk and p == "/" and stk[-1] == "/":
                    stk.pop()
            stk.append(p)
        if dots == 1:
            stk.pop()
        elif dots == 2 and stk[-3] == "/":
            for _ in range(3):
                stk.pop()
            while stk and stk[-1] != "/":
                stk.pop()
        if len(stk) > 1 and stk[-1] == "/":
            stk.pop()
        if not stk:
            stk.append("/")
        return "".join(stk)