"""
53 ms runtime beats 39.73%
16.36 MB memory beats 18.22%
"""
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        def bs(idx, v, n):
            l = 0
            r = n-1
            while l <= r:
                m = (l + r) // 2
                if arr[m] >= v:
                    r = m - 1
                elif m + 1 < n and arr[m+1] < v:
                    l = m + 1
                else:
                    if m != idx:
                        return arr[m]
                    else:
                        if m - 1 >= 0:
                            return arr[m-1]
                        else:
                            return -1
            return -1
        arr = sorted(nums)
        n = len(arr)
        res = []
        for i in range(n):
            a = arr[i]
            if k - a <= 0:
                break
            ret = bs(i, k - a, n)
            if ret > 0:
                res.append(ret + a)
        return max(res) if res else -1