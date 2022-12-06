"""
Submission Result: Wrong Answer 
Input:
"))"
Output:
true
Expected:
false
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')', '{':'}', '[':']'}
        
        if len(s) %2 != 0:
            return False
        for st in s:
            if st in ['(', '{', '[']:
                stack.append(st)
            else:
                if len(stack) != 0:
                    if st == dic[stack[-1]]:
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        
        return False
