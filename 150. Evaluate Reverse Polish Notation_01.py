'''
Submission Result: Wrong Answer 
Input:
["4","-2","/","2","-3","-","-"]
Output:
-6
Expected:
-7
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        
        for t in tokens:
            if t == "+":
                x = stk.pop()
                y = stk.pop()
                f = int(y)+int(x)
                stk.append(str(f))
            elif t == "-":
                x = stk.pop()
                y = stk.pop()
                f = int(y) - int(x)
                stk.append(str(f))
            elif t == "*":
                x = stk.pop()
                y = stk.pop()
                f = int(y) * int(x)
                stk.append(str(f))
            elif t == "/":
                x = stk.pop()
                y = stk.pop()
                f = int(y) // int(x)
                if f < 0:
                    f = f + 1
                stk.append(str(f))
            else:
                stk.append(t)
            
        return int(stk.pop())