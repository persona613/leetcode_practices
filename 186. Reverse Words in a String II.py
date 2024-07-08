"""
184 ms runtime beats 59.61%
20.92 MB memory beats 9.40%
"""
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s, l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        # reverse s and reverse all words in s
        n = len(s)
        reverse(s, 0, n - 1)
        pre_space = -1
        i = 0
        for i in range(n):
            if s[i] == " ":
                reverse(s, pre_space + 1, i - 1)
                pre_space = i
        reverse(s, pre_space + 1, n - 1)