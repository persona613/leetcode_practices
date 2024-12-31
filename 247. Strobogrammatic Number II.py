"""
151 ms runtime beats 33.38%
29.78 MB memory beats 29.56%
"""
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        def backtrack(k, res):
            if len(k) == n:
                if k[0] != "0":
                    res.add(k)
                return

            backtrack("0" + k + "0", res)
            backtrack("1" + k + "1", res)
            backtrack("8" + k + "8", res)
            backtrack("6" + k + "9", res)
            backtrack("9" + k + "6", res)

        base = [""]
        if n % 2 == 1:
            base = ["0", "1", "8"]
        if n == 1:
            return base

        res = set()
        for a in base:
            backtrack(a, res)
        return res