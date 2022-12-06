"""
accepted
"""
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(': 0, ')': 3, '[': 1, ']': 4, '{': 2, '}': 5}
        stk = []    
        sl = list(s)


        # 長度為奇數必為False
        n = len(sl)      
        if n % 2 == 1:
            return False
            
        elif n == 0:
            return False
            
        else:
            stk.append(sl.pop(0))
            while len(sl) != 0:
                stk.append(sl.pop(0))
                r1 = dic[stk[-1]]
                r2 = dic[stk[-2]]
                if r1 % 3 == r2 % 3 and r1 > r2:
                    del stk[-1:-3:-1]
                    if len(sl) == 0:
                        break
                    if len(stk) == 0:
                        stk.append(sl.pop(0))

            if len(stk) == 0:
                return True
            else:
                return False   