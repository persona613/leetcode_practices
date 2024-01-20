"""
105 ms runtime beats 5.01%
17.30 MB memory beats 12.28%
"""
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = dict()
        res = [[]]
        ln = 1 # res's length
        for v in nums:
            if v not in d:
                res[0].append(v)
                d[v] = 1
            else:
                if d[v] >= ln:
                    res.append([])
                    ln += 1
                res[d[v]].append(v)
                d[v] += 1
        return res