"""
34 ms runtime beats 57.73%
16.51 MB memory beats 36.95%
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:

        def bitadd(x, y):
            # diff bit
            xor = x ^ y
            # two 1-bit
            carry = x & y
            # do carry
            for i in range(11):
                mask = 1 << i
                d = carry & mask
                if d == 0:
                    continue
                # find xor's 0-bit for carry's 1-bit
                for j in range(1, 11 - i):
                    d <<= 1
                    # two 1-bit still carry advance
                    # and flip curr to 0
                    if (xor & d) != 0:
                        xor &= ~d
                    else:
                        xor ^= d
                        break
            return xor

        # bit complete code: positive <=> negtive
        def bitcom(x):
            return bitadd(~x, 1)

        def bitminus(x, y):
            neg = min(x, y)
            pos = max(x, y)
            if abs(neg) > pos:
                # exclude signed bit
                mask = 1 << 32
                neg &= ~mask
                # add bits except signed bit
                ret = bitadd(neg, pos)
                return ret ^ mask
            elif abs(neg) < pos:
                # reverse calculate
                ret = bitminus(bitcom(x), bitcom(y))
                return bitcom(ret)
            else:
                return 0

        if a < 0 and b < 0:
            # transfer to positive int and add
            ret = bitadd(bitcom(a), bitcom(b))
            # back to negtive int
            return bitcom(ret)

        if a < 0 or b < 0:
            return bitminus(a, b)

        return bitadd(a, b)