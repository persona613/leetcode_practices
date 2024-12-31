"""
36 ms runtime beats 73.05%
16.53 MB memory beats 37.00%
"""
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # transform int
        tran = 0
        for c in s:
            i = ord(c)-96
            tran += i // 10 + i % 10

        for _ in range(k - 1):
            tmp = 0
            while tran:
                tmp += tran % 10
                tran //= 10
            tran = tmp
            if tran < 10:
                break
        return tran