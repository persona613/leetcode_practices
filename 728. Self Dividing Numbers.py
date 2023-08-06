"""
55 ms runtime beats 83.70%
16.4 MB memory beats 6.23%
"""
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right+1):
            q = num
            ans = True
            while q:
                if q % 10 == 0 or num % (q % 10) != 0:
                    ans = False
                    break
                q = q // 10
            if ans:
                res.append(num)
        return res
        