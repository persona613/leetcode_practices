"""
Time Limit Exceeded
33 / 45 testcases passed
"""
class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        # A = N1 - N2, B = N2 - N1
        # val(A) > val(B) => bisect_left, id(A) < id(B) => bisect_right
        n = len(nums1)
        A = []
        B = []
        for i in range(n):
            A.append((nums1[i] - nums2[i], i))
            B.append((nums2[i] - nums1[i], i))

        ans = 0
        B.sort(key = lambda x: (x[0], x[1]))
        for i in range(n):
            aval, ai = A[i]
            # find idx of B where val(B) before idx(exclude) < val(A)
            # count of val(B) < val(A)
            r = bisect.bisect_left(B, aval, key = lambda x: x[0])
            # print(f"i={i}, r={r}")
            # count of B where id(b) > id(A)
            if r == n:
                ans += n - i - 1
            else:
                for j in range(r):
                    if B[j][1] > ai:
                        ans += 1
                # C = sorted(B[:r], key = lambda x: x[1])
                # l = bisect.bisect_right(C, ai, key = lambda x: x[1])
                # ans += r - l
        return ans