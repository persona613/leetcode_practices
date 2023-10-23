"""
Wrong Answer
58 / 62 testcases passed
Editorial
Input
nums = [8,5,9,9,8,4]

Use Testcase
Output 0
Expected 2
"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        lst = sorted(nums)
        mi = lst[0]
        mx = lst[-1]
        dx = len(nums)-1
        if mx-mi == dx: return 0

        arr = []
        pre = None
        for nu in lst:
            if nu != pre:
                pre = nu
                arr.append(nu)
        # print(arr)
        
        # cost of duplicate elements
        cost1 = (dx+1)-len(arr)

        def bs(arr, l, r, t):
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
        cost2 = dx
        la = len(arr)
        for i, a in enumerate(arr):
            j = bs(arr, i, la-1, a+dx)
            # print(i, j)
            save = j-i+1
            cost2 = min(cost2, la-save)
        return cost1+cost2
