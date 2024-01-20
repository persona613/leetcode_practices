"""
41 ms runtime beats 50.82%
16.35 MB memory beats 15.29%
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def fac(n):
            ret = []
            for i in range(1, n+1):
                if n % i == 0:
                    ret.append(i)
            return ret

        def check(sr, sb):
            n = len(sb)
            for i in range(len(sr)):
                if sr[i] != sb[i%n]:
                    return False
            return True

        gcd = math.gcd(len(str1), len(str2))
        divs = fac(gcd)
        for d in divs[::-1]:
            sb = str1[:d]
            if check(str1, sb) and check(str2, sb):
                return sb
        return ""