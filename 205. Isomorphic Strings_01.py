'''
Input:
"badc"
"baba"
Output:
true
Expected:
false
'''
# Failure
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        for i, n in enumerate(s):
           
            if n in dic:
                if dic[n] == t[i]:
                    pass
                else:
                    return False
            else:
                dic[n] = t[i]
        return True