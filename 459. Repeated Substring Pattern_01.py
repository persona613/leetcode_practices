"""Wrong Answer
122 / 129 testcases passed
Input
s = "abacababacab"
Output
false
Expected
true
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 1: return False
        maxsub = 1
        for i in range(2, math.ceil(n/2)+1):
            if n % i == 0:
                maxsub = n // i
                break
        # i: main loop index, j: sub string index
        i, j = 1, 0
        # k: sub string length
        k = 1
        while i < n:
            if s[i] == s[j]:
                if n % k == 0:
                    i += 1
                    j += 1
                else:
                    i += 1
                    j = 0
            else:
                if i >= maxsub:
                    return False
                else:
                    i += 1
                    j = 0
                    k = i
        return True
