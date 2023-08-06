"""
37 ms runtime beats 96.23%
16.3 MB memory beats 35.65%
"""
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i, j = 0, len(s)-1
        lst = list(s)
        while i <= j:
            if not lst[i].isalpha():
                i += 1
                continue
            if not lst[j].isalpha():
                j -= 1
                continue
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
        return "".join(lst)