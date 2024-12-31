"""
182 ms runtime beats 63.42%
17.01 MB memory beats 63.10%
"""
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        ln = 1
        cur_end = pairs[0][1]
        for p in pairs[1:]:
            if cur_end < p[0]:
                ln += 1
                cur_end = p[1]
        return ln