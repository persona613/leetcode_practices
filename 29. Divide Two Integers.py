"""
33 ms runtime beats 79.90%
16.58 MB memory beats 54.32%
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = dividend
        d = divisor

        negtive = False
        if (n < 0 and d > 0) or (n > 0 and d < 0):
            negtive = True

        # handel out-range
        plus = 0
        if n == -2 ** 31:
            # prevent q out-range in 2 cases
            if d == -1:
                return 2 ** 31 - 1
            elif d == 1:
                return n
            n = 2 ** 31 - 1
            plus = 1

        n = abs(n)
        d = abs(d)
        # quotient
        q = 0
        # remainder
        r = 0
        # binary long division
        for i in range(30, -1, -1):
            mask = 1 << i

            # expand remainder bit from dividend
            r <<= 1
            if n & mask:
                r |= 1

            q <<= 1
            if r >= d:
                r -= d
                q |= 1

        # out-range plus
        if plus and plus + r >= d:
            q += 1
        return ~q + 1 if negtive else q
                