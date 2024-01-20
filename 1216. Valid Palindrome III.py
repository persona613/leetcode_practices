"""
1190 ms runtime beats 17.85%
274.84 MB memory beats 19.13%
"""
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = dict()
        def remove(i, j, d):
            if (i, j, d) in memo:
                return memo[(i, j, d)]
            if s[i] == s[j]:
                if i == j or i + 1 == j:
                    memo[(i, j, d)] = True
                else:
                    memo[(i, j, d)] = remove(i + 1, j - 1, d)
            else:
                if d == 0:
                    memo[(i, j, d)] = False
                else:
                    memo[(i, j, d)] = remove(i + 1, j, d - 1) \
                                      or remove(i, j - 1, d - 1)
            return memo[(i, j, d)]
        return remove(0, len(s) - 1, k)