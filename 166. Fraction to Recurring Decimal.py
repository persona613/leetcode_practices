"""
27 ms runtime beats 94.01%
16.82 MB memory beats 21.98%
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = []
        n = numerator
        p = denominator

        # pre adjust negtive division in python
        if n * p < 0:
            res.append("-")
            n = abs(n)
            p = abs(p)

        # interger part
        q = n // p
        r = n % p
        res.append(str(q))
        if not r:
            return "".join(res)
        
        # fraction part
        # maintain dict: {(remainder, quotient): index}
        # for detect repeating and index for insert "("
        res.append(".")
        seen = dict()
        while r:
            r *= 10
            q = r // p
            r = r % p
            if (r, q) in seen:
                res.insert(seen[(r, q)], "(")
                res.append(")")
                break

            seen[(r, q)] = len(res)
            res.append(str(q))
        return "".join(res)