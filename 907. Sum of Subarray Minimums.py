"""
385 ms runtime beats 48.39%
21.79 MB memory beats 62.28%
"""
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # ans += arr[i] * (1+L+R+L*R = L*R)
        # record next-min-index by monotonic stack
        n = len(arr)

        # left range for next-min-index
        lg = [None] * n
        stk = [(arr[n-1], n-1)]
        for i in range(n-2, -1, -1):
            a = arr[i]
            while stk and stk[-1][0] >= a: # "=" for remove duplicate left-count
                pre = stk.pop()
                lg[pre[1]] = i # next-min-index
            stk.append((a, i))
        while stk:
            lg[stk.pop()[1]] = -1

        # right range for next-min-index
        rg = [None] * n
        stk = [(arr[0], 0)]
        for i in range(1, n):
            a = arr[i]
            while stk and stk[-1][0] > a:
                pre = stk.pop()
                rg[pre[1]] = i # next-min-index
            stk.append((a, i))
        while stk:
            rg[stk.pop()[1]] = n

        ans = 0
        for i in range(n):
            ans += arr[i] * (i - lg[i]) * (rg[i] - i)
        return ans % (10**9 + 7)
