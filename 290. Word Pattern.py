"""
50 ms runtime beats 9.11%
16.3 MB memory beats 10.34%
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split()
        if len(pattern) != len(lst):
            return False

        p2s = {} # {pattern[i]: lst[i]}
        s2p = {} # {lst[i]: pattern[i]}
        for i in range(len(pattern)):
            if not p2s.get(pattern[i]):
                p2s[pattern[i]] = lst[i]
            else:
                if p2s[pattern[i]] != lst[i]:
                    return False
            if not s2p.get(lst[i]):
                s2p[lst[i]] = pattern[i]
            else:
                if s2p[lst[i]] != pattern[i]:
                    return False                
        return True
