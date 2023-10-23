"""
85 ms runtime beats 76.62%
16.5 MB memory beats 43.69%
"""
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def bs(lst, n, t):
            l, r = 0, n-1
            while l <= r:
                m = (l+r)//2
                if t == lst[m]:
                    return t, t
                elif t > lst[m]:
                    l = m+1
                else:
                    r = m-1
            if l > n-1: l = n-1
            if r < 0: r = 0
            return lst[r], lst[l]
        lst = sorted(arr2)
        n = len(arr2)
        ans = 0
        for a in arr1:
            p1, p2 = bs(lst, n, a)
            pd = min(abs(a-p1), abs(a-p2))
            if pd > d:
                ans += 1
        return ans