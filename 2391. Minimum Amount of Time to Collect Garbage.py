"""
771 ms runtime beats 96.20%
39.40 MB memory beats 34.21%
"""
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # travel time
        tm = [0]
        for tr in travel:
            tm.append(tm[-1]+tr)
        # garbage count
        gt = 0
        for g in garbage:
            gt += len(g)
        tp = "MPG"
        idx = []
        for p in tp:
            for i in range(len(garbage)-1, -1, -1):
                if p in garbage[i]:
                    idx.append(i)
                    break
        for i in idx:
            gt += tm[i]
        return gt
