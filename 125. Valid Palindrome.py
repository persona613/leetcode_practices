"""
55 ms runtime beats 33.84%
14.8 MB memory beats 44.64%
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l <= r:
            while l<len(s) and (not s[l].isalnum()):
                l += 1
            while r>-1 and (not s[r].isalnum()):
                r -= 1
            if l>=len(s) and r<=-1:
                break
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
