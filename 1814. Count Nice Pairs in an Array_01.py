"""
Wrong Answer
81 / 84 testcases passed
"""
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(u):
            tmp = []
            while u:
                tmp.append(u % 10)
                u //= 10
            n = len(tmp)-1
            r = 0
            for i, t in enumerate(tmp):
                r += t*(10**(n-i))
            return r
        arr = []
        d = dict()
        ans = 0
        for u in nums:
            arr.append(u - rev(u))
        for a in arr:
            if a in d:
                ans += d[a]
                d[a] += 1
            else:
                d[a] = 1
        return ans