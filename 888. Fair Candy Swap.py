"""
497 ms runtime beats 28.10%
18.7 MB memory beats 70.86%
"""
class Solution:
    def bs(self, tg, lst):
        l, r = 0, len(lst)-1
        while l <= r:
            m = (l+r) // 2
            if tg == lst[m]:
                return m
            elif tg < lst[m]:
                r = m-1
            else:
                l = m+1
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        searched = set()
        asum, bsum = sum(aliceSizes), sum(bobSizes)
        diff = (asum+bsum)/2 - asum
        bobSizes.sort()
        for num in aliceSizes:
            if num in searched:
                continue
            tg = num + diff
            k = self.bs(tg, bobSizes)
            if k != None:
                return [num, bobSizes[k]]
            searched.add(num)