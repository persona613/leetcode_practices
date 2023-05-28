"""
7880 ms runtime beats 5.2%
16.1 MB memory beats 42.64%
"""
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False
        divisors = [1]
        for di in range(2, (num//2)+1):
            if num % di == 0:
                if di in divisors:
                    break
                divisors.extend(set([di, num//di]))
        # print(divisors)
        return sum(divisors) == num