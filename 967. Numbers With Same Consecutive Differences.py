"""
36 ms runtime beats 87.32%
16.79 MB memory beats 93.15%
"""
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        def backtrack(i, val, pre):
            if i == n:
                res.append(val)
                return

            val *= 10
            for j in range(10):
                if abs(j - pre) == k:
                    val += j
                    backtrack(i + 1, val, j)
                    val -= j

        res = []
        for v in range(1, 10):
            # (index, val, pre-digit)
            backtrack(1, v, v)
        return res