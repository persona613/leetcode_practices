"""
67 ms runtime beats 80.56%
17.60 MB memory beats 50.24%
"""
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m = len(str1)
        n = len(str2)
        i = j = 0
        while i < m and j < n:
            if str1[i] == str2[j] or (ord(str2[j]) - ord(str1[i])) % 26 == 1:
                j += 1
            i += 1
        return j == n