"""
1352 ms runtime beats 10.94%
59.84 MB memory beats 6.25%
"""
class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        # A = N1 - N2, B = N2 - N1
        # val(A) > val(B) => bisect_left
        n = len(nums1)
        A = []
        B = []
        for i in range(n):
            A.append((nums1[i] - nums2[i], i))
            B.append((nums2[i] - nums1[i], i))

        ans = 0
        C = sorted(B, key = lambda x: (x[0], x[1]))
        for i in range(n):
            aval = A[i][0]
            # find idx of B where val(B) before idx(exclude) < val(A)
            # count of val(B) < val(A)
            r = bisect.bisect_left(C, aval, key = lambda x: x[0])
            ans += r
            # remove pair: i == j
            if B[i][0] < aval:
                ans -= 1
        return ans // 2 # deduct duplicate pairs, (i, j)<=>(j, i)