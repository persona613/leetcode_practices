"""
65 ms runtime beats 87.26%
17.33 MB memory beats 72.36%
"""
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        
        # k: bigger part factor
        # f: start factor to find combination
        def backtrack(k, f, comb):
            for d in range(f, int(k ** 0.5) + 1):
                if k % d == 0:
                    comb.append(d)
                    backtrack(k // d, d, comb)
                    comb.pop()
                    
            comb.append(k)
            res.append(comb[:])
            comb.pop()

        res = []
        comb = []
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                comb.append(d)
                backtrack(n // d, d, comb)
                comb.pop()
        return res