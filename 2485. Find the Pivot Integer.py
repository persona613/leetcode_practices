"""
45 ms runtime beats 64.82%
16.57 MB memory beats 59.17%
"""
class Solution:
    def pivotInteger(self, n: int) -> int:
        presum = [0]
        sm = 0
        for i in range(1, n+1):
            sm += i
            presum.append(sm)
        for i in range(1, n+1):
            if presum[i] == sm - presum[i] + i:
                return i
        return -1