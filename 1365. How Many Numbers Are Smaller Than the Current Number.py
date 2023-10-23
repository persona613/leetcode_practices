"""
57 ms runtime beats 87.69%
16.3 MB memory beats 88.92%
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        acc = dict()
        for i in range(len(arr)):
            a = arr[i]
            if a not in acc:
                acc[a] = i
        res = []
        for a in nums:
            res.append(acc[a])
        return res


        # dc = Counter(nums)
        # ars = sorted(dc.keys())
        # n = len(ars)
        # acc = [0] * n # accumulate cnt
        # for i in range(1, n):
        #     acc[i] = acc[i-1] + dc[ars[i-1]]
        # res = []
        # for v in nums:
        #     res.append(acc[ars.index(v)])
        # return res


        # dc = Counter(nums)
        # ars = sorted(dc.keys())
        # n = len(ars)
        # acc = dict()
        # acc[ars[0]] = 0
        # for i in range(1, n):
        #     v = ars[i]
        #     pv = ars[i-1]
        #     acc[v] = acc[pv] + dc[pv]
        # res = []
        # for v in nums:
        #     res.append(acc[v])
        # return res