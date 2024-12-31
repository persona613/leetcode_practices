"""
291 ms runtime beats 5.07%
17.52 MB memory beats 26.73%
"""
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # find the number of all pairs that diff <= x
        def findpairs(diff):
            ans = 0
            for i in range(0, n - 1):
                base = arr[i]
                l, r = i + 1, n - 1
                # bisect_right
                while l <= r:
                    mid = (l + r) // 2
                    d = arr[mid] - base
                    if d <= diff:
                        l = mid + 1
                    else:
                        r = mid - 1
                ans += r - i
            return ans

        arr = sorted(nums)
        n = len(arr)
        # find diff range
        r = arr[-1] - arr[0]
        l = inf
        for i in range(1, n):
            if arr[i] - arr[i - 1] < l:
                l = arr[i] - arr[i - 1]
                if l == 0:
                    break
        # bisect_left
        while l <= r:
            mid = (l + r) // 2
            pairs = findpairs(mid)
            if k <= pairs:
                r = mid - 1
            else:
                l = mid + 1
        return l