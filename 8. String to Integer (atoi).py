"""
39 ms runtime beats 50.10%
16.64 MB memory beats 18.60%
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        MIN = -(2 ** 31)
        MAX = 2 ** 31 - 1
        bag = []
        sign = ""
        for c in s:
            if c == " " and not sign and not bag:
                continue
            elif c == "-" and not sign and not bag:
                sign = "-"
            elif c == "+" and not sign and not bag:
                sign = "+"
            elif c.isdigit():
                bag.append(c)
            else:
                break
        if not bag:
            return 0

        n = int(sign + "".join(bag))
        if n < MIN:
            return MIN
        elif n > MAX:
            return MAX
        return n 