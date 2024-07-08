"""
Wrong Answer
15 / 20 testcases passed

Editorial
Input
pattern =
"ab"
s =
"aa"

Use Testcase
Output
true
Expected
false
"""
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        def backtrack(i, j):
            if i == m:
                return True

            curr = pattern[i]
            # had map: p -> q
            if curr in dic:
                d = len(dic[curr])
                if dic[curr] != s[j: j + d]:
                    return False
                return backtrack(i + 1, j + d)

            # not yet had map: p-> q
            for d in range(1, n - j + 1):
                q = s[j : j + d]
                dic[curr] = q
                ret = backtrack(i + 1, j + d)
                if ret:
                    return True
            return False
        
        m = len(pattern)
        n = len(s)
        dic = dict()
        return backtrack(0, 0)