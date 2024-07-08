"""
63 ms runtime beats 42.63%
18.56 MB memory beats 82.57%
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # two counter
        # ones: 00->01
        # twos: 01->10 (every 3 times = 0)
        ones = twos = 0
        for val in nums:
            # 10->00, carry needed to threes
            carry = val & twos
            twos ^= carry
            val ^= carry

            # 01->10, carry needed to twos
            carry = val & ones
            # cancel 1-bit because carry
            val ^= carry
            ones ^= carry
            # carry to twos, 10->00(3 times = 0)
            twos ^= carry
            # 00->01, add
            ones ^= val
        return ones + twos