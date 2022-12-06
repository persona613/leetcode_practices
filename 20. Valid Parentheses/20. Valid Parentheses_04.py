"""
Status: Wrong Answer
Input:
"(("
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
                if st == dic[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return True