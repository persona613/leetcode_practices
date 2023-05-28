"""
81 ms runtime beats 19.51%
17.4 MB memory beats 5.62%
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        vowels = ["a", "e", "i", "o", "u"]
        lst = list(s)
        while l <= r:
            while lst[l].lower() not in vowels and l<=r:
                l += 1
                if l > len(s)-1:
                    break
            while lst[r].lower() not in vowels and l<=r:
                r -= 1
            if l <= r:
                lst[l], lst[r] = lst[r], lst[l]
                l += 1
                r -= 1
        return "".join(lst)