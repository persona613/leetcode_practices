"""
207 ms runtime beats 82.58%
16.83 MB memory beats 64.12%
"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dt = defaultdict(int)
        g = defaultdict(int)
        arr = sorted(nums)
        cnt, elm = 0, 0
        for i in range(len(arr)):
            a = arr[i]
            pcnt, pelm = 0, 0
            for j in range(i - 1, -1, -1):
                d = arr[j]
                if a % d == 0 and dt[d] > pcnt:
                    pcnt = dt[d]
                    pelm = d
            dt[a] = pcnt + 1
            g[a] = pelm
            if dt[a] > cnt:
                cnt = dt[a]
                elm = a
            
        res = []
        while elm:
            res.append(elm)
            elm = g[elm]
        print(arr)
        return res
                