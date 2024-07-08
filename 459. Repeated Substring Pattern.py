"""
43 ms runtime beats 66.51%
16.75 MB memory beats 32.17%
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 1: return False
        maxsub = n //2 + 1
        for k in range(1, maxsub):
            if n % k:
                continue
            substring = s[:k]
            for i in range(1, n // k):
                nxt_substring = s[i * k: i * k + k]
                if substring != nxt_substring:
                    break
            else:
                return True
        return False