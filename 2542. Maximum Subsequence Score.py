"""
701 ms runtime beats 99.08%
37.19 MB memory beats 70.12%
"""
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr = list(zip(nums2, nums1))
        arr.sort()
        n = len(arr)

        # k max heap, maintain bigger vals of num1
        q = []
        asum = 0
        for i in range(n-1, n-1-k, -1):
            asum += arr[i][1]
            heappush(q, arr[i][1])
        ans = asum * arr[n-k][0]

        for i in range(n-1-k, -1, -1):
            # if new val <= q[0]
            # no need consider while both array decrease
            if arr[i][1] > q[0]:
                # minus minin val
                asum += arr[i][1] - heappop(q)
                heappush(q, arr[i][1])

                # calculate new product
                if asum * arr[i][0] > ans:
                    ans = asum * arr[i][0]
        return ans