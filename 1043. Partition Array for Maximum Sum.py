"""
137 ms runtime beats 98.32%
16.62 MB memory beats 78.54%
"""
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # max sum
            mxsm = 0
            # max element
            ma = arr[i - 1]
            for t in range(1, k+1):
                if i - t < 0:
                    break
                if arr[i - t] > ma:
                    ma = arr[i - t]
                sm = dp[i - t] + ma * t
                if sm > mxsm:
                    mxsm = sm
            dp[i] = mxsm
            
        return dp[-1]
                