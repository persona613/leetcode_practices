"""
Submission Result: Wrong Answer 
Input:
"/hello./world/"
Output:
"/hello/world"
Expected:
"/hello./world"
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        dots = 0
        for p in path:
            if p == ".":
                dots += 1
            else:
                if dots == 1 and p =="/":
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