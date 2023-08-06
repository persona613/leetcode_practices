"""
797 ms runtime beats 68%
20.3 MB memory beats 68.32%
"""
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        b5, b10 = 0, 0
        for b in bills:
            if b == 5:
                b5 += 1
                continue
            elif b == 10:
                b10 += 1
                b5 -= 1
            else:
                if b10 > 0:
                    b10 -= 1
                    b5 -= 1
                else:
                    b5 -= 3
            if b5 < 0:
                return False
        return True