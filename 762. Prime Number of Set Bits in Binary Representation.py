"""
227 ms runtime beats 74.32%
16.4 MB memory beats 9.29%
"""
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        cnt = 0
        primes = [2,3,5,7,11,13,17,19]
        for i in range(left, right+1):
            if bin(i)[2:].count("1") in primes:
                cnt += 1
        return cnt