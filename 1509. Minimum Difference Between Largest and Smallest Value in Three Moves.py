"""
305 ms runtime beats 8.26%
27.30 MB memory beats 72.88%
"""
class Solution:
    def minDifference(self, nums: List[int]) -> int:

        def comb(arr):
            if len(arr) < 4:
                return 0

            arr.sort()
            return min(
                arr[-4] - arr[0],
                arr[-3] - arr[1],
                arr[-2] - arr[2],
                arr[-1] - arr[3]
            )

        if len(nums) <= 8:
            return comb(nums)

        # take min 4 nums
        mxheap = []
        # take max 4 nums
        miheap = []
        for num in nums:
            heappush(mxheap, -num)
            if len(mxheap) > 4:
                heappop(mxheap)
            
            heappush(miheap, num)
            if len(miheap) > 4:
                heappop(miheap)
        return comb([-v for v in mxheap] + miheap)