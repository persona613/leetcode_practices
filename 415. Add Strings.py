"""
69 ms runtime beats 5.57%
16.9 MB memory beats 6.6%
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        summ = []
        n1, n2 = len(num1), len(num2)
        if n1 >= n2:
            big, small = num1, num2
        else:
            big, small = num2, num1
        i, q = -1, 0
        while i > -len(big)-1:
            if i > -len(small)-1:
                k = int(big[i]) + int(small[i]) + q
            else:
                k = int(big[i]) + q
            r = k % 10
            q = k // 10
            summ.append(str(r))
            i -= 1
        if q:
            summ.append(str(q))
        return ''.join(summ[::-1])
