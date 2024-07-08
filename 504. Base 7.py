"""
35 ms runtime beats 53.93%
16.50 MB memory beats 94.79%
"""
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        n = abs(num)
        dgs = []
        while n > 0:
            dgs.append(str(n % 7))
            n //= 7
        if num < 0:
            dgs.append("-")
        return "".join(dgs)[::-1]