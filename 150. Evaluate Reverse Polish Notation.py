'''
Runtime: 65 ms, faster than 74.38% of Python3 online submissions 
Memory Usage: 17.22 MB, less than 58.04% of Python3 online submissions 
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        stk = []
        for t in tokens:
            if t in ops:
                op = ops[t]
                y = stk.pop()
                x = stk.pop()
                stk.append(op(x, y))
            else:
                stk.append(int(t))
                
        return stk.pop()