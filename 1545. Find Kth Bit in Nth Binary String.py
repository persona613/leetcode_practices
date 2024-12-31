"""
0 ms runtime beats 100%
16.63 MB memory beats 56.21%
"""
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Si length
        slen = [0] * (n + 1)
        for i in range(1, n + 1):
            slen[i] = slen[i - 1] * 2 + 1

        def find(i, t):
            if i == 1:
                return 0

            # length of S_i-1
            ln = slen[i - 1]
            # mid point, one-index
            if t == ln + 1:
                return 1
            elif t < ln + 1:
                return find(i - 1, t)
            else:
                # new index = t at S_i-1 index = t - (ln + 1)
                # reverse new index = ln - new_index + 1
                return find(i - 1, 2 * ln - t + 2) ^ 1
        
        return str(find(n, k))