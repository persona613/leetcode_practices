"""
31 ms runtime beats 81.95%
16.54 MB memory beats 36.09%
"""
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        def backtrack(i, j):
            if i == m:
                if j == n:
                    return True
                return False

            curr = pattern[i]
            # had map: p -> q
            if curr in dic:
                d = len(dic[curr])
                if dic[curr] != s[j: j + d]:
                    return False
                return backtrack(i + 1, j + d)

            # not yet had map: p -> q
            for d in range(1, n - j + 1):
                q = s[j : j + d]
                if q in pool:
                    continue
                pool.add(q)
                dic[curr] = q
                ret = backtrack(i + 1, j + d)
                if ret:
                    return True
                pool.remove(q)
                del dic[curr]

            return False
        
        m = len(pattern)
        n = len(s)
        dic = dict()
        pool = set()
        return backtrack(0, 0)