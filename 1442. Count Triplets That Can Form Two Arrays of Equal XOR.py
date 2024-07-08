"""
34 ms runtime beats 94.25%
16.72 MB memory beats 14.37%
"""
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        dic = defaultdict(set)
        dic[0].add(-1)
        curr = ans = 0
        for i in range(len(arr)):
            curr ^= arr[i]
            for prei in dic[curr]:
                # if i - prei >= 2 :
                # (no need bcz no zero, never length=1)
                ans += i - prei - 1

            # record each prexor of end index
            dic[curr].add(i)
        return ans


        # xors = [0]
        # for a in arr:
        #     xors.append(xors[-1] ^ a)
        # ans = 0
        # for ln in range(2, len(arr) + 1):
        #     for k in range(ln, len(xors)):
        #         xorsum = xors[k] ^ xors[k - ln]
        #         if xorsum == 0:
        #             ans += ln - 1
        # return ans