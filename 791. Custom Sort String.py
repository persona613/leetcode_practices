"""
27 ms runtime beats 98.47%
16.99 MB memory beats 25.97%
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        bag = Counter(s)
        for o in order:
            if o in bag:
                res.extend([o] * bag[o])
                del bag[o]
        for k in bag:
            res.extend([k] * bag[k])
        return "".join(res)