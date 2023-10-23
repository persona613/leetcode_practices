"""
1793 ms runtime beats 5.26%
31 MB memory beats 100%
"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dx = len(nums)-1
        lst = sorted(nums)
        arr = []
        pre = None
        for nu in lst:
            if nu != pre:
                pre = nu
                arr.append(nu)
        # print(arr)

        # cost of duplicate elements
        cost1 = (dx+1)-len(arr)
        if cost1 == 0:
            mi = arr[0]
            mx = arr[-1]
            if mx-mi == dx: return 0
            
        cost2 = dx
        la = len(arr)
        for i, a in enumerate(arr):
            j = self.bs(arr, i, la-1, a+dx)
            # print(i, j)
            save = j-i+1
            cost2 = min(cost2, la-save)

        return cost1+cost2


    def bs(self, arr, l, r, t):
        st = l
        nd = r
        while l <= r:
            m = (l+r)//2
            if arr[m] == t:
                return m
            elif arr[m] < t:
                if m+1 <= nd and arr[m+1] > t:
                    return m
                else:
                    l = m+1
            else:
                if m-1 >= st and arr[m-1] < t:
                    return m-1
                else:
                    r = m-1
        return nd