"""
1357 ms runtime beats 98.45%
71.98 MB memory beats 43.55%
"""
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        cnt = dict()
        for w, l in matches:
            cnt[w] = cnt.get(w, 0)
            cnt[l] = cnt.get(l, 0) + 1
        a0 = []
        a1 = []
        for k in cnt:
            if cnt[k] == 0:
                a0.append(k)
            elif cnt[k] == 1:
                a1.append(k)
        return [sorted(a0), sorted(a1)]
                