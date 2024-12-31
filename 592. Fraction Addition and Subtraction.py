"""
39 ms runtime beats 34.11%
16.56 MB memory beats 59.69%
"""
class Solution:
    def fractionAddition(self, expression: str) -> str:

        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            if a % b == 0:
                return b
            return gcd(b, a % b)
        
        def lcm(a, b):
            k = gcd(a, b)
            return k * (a // k) * (b // k)

        def cal(a, b, c, d):
            lm = lcm(b, d)
            numerator = a * (lm // b) + c * (lm // d)
            if numerator == 0:
                return 0, 1
            gd = gcd(abs(numerator), lm)
            return numerator // gd, lm // gd

        stk = expression[0] + expression[1:].replace("-", "+-")
        stk = stk.split("+")
        pair = stk.pop().split("/")
        a, b = int(pair[0]), int(pair[1])
        while stk:
            pair = stk.pop().split("/")
            c, d = int(pair[0]), int(pair[1])
            a, b = cal(a, b, c, d)
        return str(a) + "/" + str(b)