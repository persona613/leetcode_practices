"""
34 ms runtime beats 61.78%
16.47 MB memory beats 95.07%
"""
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        chars = "abcdef"
        dic = dict()
        for i in range(10, 16):
            dic[i] = chars[i - 10]
        
        # turn into binary digits
        val = abs(num)
        dgs = []
        while val:
            dgs.append(val % 2)
            val //= 2

        # -a = 1 + ~a = ~(a - 1)
        if num < 0:
            # pad zero
            if len(dgs) < 32:
                dgs.extend([0] * (32 - len(dgs)))

            # ~a
            dgs = [1 ^ i for i in dgs]

            # ~a + 1
            i = 0
            while dgs[i] == 1:
                dgs[i] = 0
                i += 1
            dgs[i] = 1
            
        # four binary-digits = one 16-digit
        res = []
        for i in range(0, len(dgs), 4):
            d = 0
            for j in range(min(len(dgs) - i, 4)):
                d += dgs[i + j] << j
            if d >= 10:
                res.append(dic[d])
            else:
                res.append(str(d))
        return "".join(res)[::-1]