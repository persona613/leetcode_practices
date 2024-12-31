"""
127 ms runtime beats 26.33%
16.69 MB memory beats 36.75%
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        q = [1]
        k = last = 0
        while k < n:
            # duplicate number
            while last == q[0]:
                heappop(q)
            last = heappop(q)
            k += 1

            # generate next step ugly number
            heappush(q, last * 2)
            heappush(q, last * 3)
            heappush(q, last * 5)
        return last
        