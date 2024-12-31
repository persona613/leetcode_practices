"""
55 ms runtime beats 47.82%
16.67 MB memory beats 20.67%
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        res = [0] * (m + n)

        # multyply digit
        arr1 = [ord(c) - ord("0") for c in num1[::-1]]
        arr2 = [ord(c) - ord("0") for c in num2[::-1]]
        for i in range(m):
            for j in range(n):
                # prod = a * b * 10 ** (i + j)
                prod = arr1[i] * arr2[j]
                # ten power
                k = i + j
                res[k] += prod % 10
                res[k + 1] += prod // 10
        # carry
        for i in range(m + n):
            if res[i] > 9:
                res[i + 1] += res[i] // 10
                res[i] = res[i] % 10
        
        while res and res[-1] == 0:
            res.pop()

        return "".join([str(i) for i in res])[::-1] if res else "0"
        