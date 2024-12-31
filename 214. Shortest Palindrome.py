"""
58 ms runtime beats 78.12%
20.82 MB memory beats 19.34%
"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # KMP algorithm, longest proper prefix suffix
        text = s + "#" + s[::-1]
        n = len(text)
        LPS = [0] * n
        # curr string's lps_length
        i = 1
        length = 0
        while i < n:
            if text[i] == s[length]:
                length += 1
                LPS[i] = length
                i += 1
            else:
                if length == 0:
                    # LPS[i] = 0
                    i += 1
                else:
                    length = LPS[length - 1]
        k = LPS[-1]
        return s[k:][::-1] + s