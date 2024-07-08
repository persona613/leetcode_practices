"""
50 ms runtime beats 33.95%
16.47 MB memory beats 87.76%
"""
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s = set(source)
        t = set(target)
        for c in t:
            if c not in s:
                return -1
        
        i = j = cnt = 0
        n = len(source)
        while j < len(target):
            if source[i] == target[j]:
                i += 1
                j += 1
            else:
                i += 1

            if i == n:
                # print(cnt, j)
                cnt += 1
                i = 0
        return cnt if i == 0 else cnt + 1