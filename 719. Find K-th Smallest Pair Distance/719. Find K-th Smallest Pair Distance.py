"""
75 ms runtime beats 98.07%
17.50 MB memory beats 16.16%
"""
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # find the number of all pairs that diff <= x
        def findpairs(diff):
            cnt = l = 0
            for r in range(n):
                while arr[r] - arr[l] > diff:
                    l += 1
                cnt += r - l
            return cnt

        arr = sorted(nums)
        n = len(arr)
        # solution space
        r = arr[-1] - arr[0]
        l = 0
        while l < r:
            mid = (l + r) // 2
            pairs = findpairs(mid)
            if k <= pairs:
                r = mid
            else:
                l = mid + 1
        return l