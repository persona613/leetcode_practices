'''
Runtime: 141 ms, faster than 57.63% of Python3 online submissions 
Memory Usage: 14.4 MB, less than 60.68% of Python3 online submissions 
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
                f = int(y) / int(x)
                f = int(f)
                stk.append(str(f))
            else:
                stk.append(t)
            
        return int(stk.pop())
