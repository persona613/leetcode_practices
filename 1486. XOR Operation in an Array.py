"""
39 ms runtime beats 50.26%
16.18 MB memory beats 71.68%
"""
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        for i in range(1, n):
            ans ^= start + 2*i
        return ans

        # arr = [None]*n
        # for i in range(n):
        #     arr[i] = start + 2*i
        # ans = arr[0]
        # for a in arr[1:]:
        #     ans ^= a
        # return ans