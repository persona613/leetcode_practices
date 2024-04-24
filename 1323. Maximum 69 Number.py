"""
34 ms runtime beats 61.07%
16.51 MB memory beats 35.36%
"""
class Solution:
    def maximum69Number (self, num: int) -> int:
        first_six = -1
        digit = 0
        val = num
        while val:
            if val % 10 == 6:
                first_six = digit
            val //= 10
            digit += 1
        return num if first_six == -1 else num + 3 * 10 ** first_six