"""
48 ms runtime beats 28.7%
16.3 MB memory beats 27.2%
"""
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        n = abs(num)
        dgs = []
        while n > 0:
            dgs.append(n % 7)
            n //= 7
        if num < 0:
            dgs.append("-")
        return "".join([str(i) for i in dgs[::-1]])