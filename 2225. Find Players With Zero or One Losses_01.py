"""
1528 ms runtime beats 82.62%
71.12 MB memory beats 56.71%
"""
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = set()
        cnt = defaultdict(int)
        for w, l in matches:
            win.add(w)
            cnt[l] += 1
        a0 = sorted(win - set(cnt))
        a1 = sorted(k for k in cnt if cnt[k]==1)
        return [a0, a1]
        