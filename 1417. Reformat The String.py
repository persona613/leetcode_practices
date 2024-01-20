"""
42 ms runtime beats 85.50%
16.20 MB memory beats 88.55%
"""
class Solution:
    def reformat(self, s: str) -> str:
        cs, ds = [], []
        for r in s:
            if r.isalpha():
                cs.append(r)
            else:
                ds.append(r)
        dif = len(cs)-len(ds)
        if dif < -1 or dif > 1:
            return ""
        if dif >= 0:
            res = [x for z in zip_longest(cs,ds,fillvalue="") for x in z]
        else:
            res = [x for z in zip_longest(ds,cs,fillvalue="") for x in z]
        return "".join(res)