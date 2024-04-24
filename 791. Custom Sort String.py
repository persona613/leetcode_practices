"""
33 ms runtime beats 73.85%
16.51 MB memory beats 61.09%
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # weight order
        wo = dict()
        # default weight
        dw = len(order)

        for i in range(dw):
            wo[order[i]] = i
        arr = sorted(s, key = lambda x: wo.get(x, dw))
        return "".join(arr)
        