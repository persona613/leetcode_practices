"""
45 ms runtime beats 71.12%
16.29 MB memory beats 79.40%
"""
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lt1 = s1.split()
        lt2 = s2.split()
        record = set()
        res = set()
        for w in lt1:
            if w not in record:
                record.add(w)
                res.add(w)
            else:
                res.discard(w)
        for w in lt2:
            if w not in record:
                record.add(w)
                res.add(w)
            else:
                res.discard(w)
        return res