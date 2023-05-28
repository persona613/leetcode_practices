"""
Wrong Answer

38 / 41 testcases passed
Input
pattern =
"abba"
s =
"dog dog dog dog"
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split()
        if len(pattern) != len(lst):
            return False

        maps = {} # {pattern[i]: s[i]}
        for i in range(len(pattern)):
            try:
                if maps[pattern[i]] != lst[i]:
                    return False
            except:
                maps[pattern[i]] = lst[i]
        return True
