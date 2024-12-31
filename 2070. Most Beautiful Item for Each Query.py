"""
129 ms runtime beats 81.71%
64.88 MB memory beats 75.27%
"""
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        m = len(items)
        items.sort()
        n = len(queries)
        qj = sorted(range(n), key = lambda j: queries[j])

        # item index, max beauty
        idx = mxb = 0
        res = [0] * n
        for j in qj:
            qp = queries[j]
            while idx < m and items[idx][0] <= qp:
                mxb = max(mxb, items[idx][1])
                idx += 1
            res[j] = mxb
        return res