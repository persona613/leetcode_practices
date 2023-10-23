"""
37 ms runtime beats 70.8%
17.2 MB memory beats 25.43%
"""
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        # find peak
        p, v = self.bs_peak(mountain_arr, 0, n-1)
        if v == target: return p

        # find left side
        idx = self.bs_lside(mountain_arr, 0, p-1, target)
        if idx != -1: return idx

        # find right side
        idx = self.bs_rside(mountain_arr, p-1, n-1, target)
        if idx != -1: return idx
        return -1

    def bs_peak(self, arr, l, r):
        while l <= r:
            m = (l+r)//2
            x = arr.get(m)
            if x<arr.get(m+1):
                l = m+1
            elif x>arr.get(m-1):
                    return m, x
            else:
                r = m-1

    def bs_lside(self, arr, l, r, t):
        while l <= r:
            m = (l+r)//2
            x = arr.get(m)
            if x == t:
                return m
            elif x < t:
                l = m+1
            else:
                r = m-1
        return -1

    def bs_rside(self, arr, l, r, t):
        while l <= r:
            m = (l+r)//2
            x = arr.get(m)
            if x == t:
                return m
            elif x > t:
                l = m+1
            else:
                r = m-1
        return -1