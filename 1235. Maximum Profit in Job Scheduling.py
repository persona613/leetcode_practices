"""
638 ms runtime beats 60.52%
61.50 MB memory beats 25.63%
"""
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def dfs(i, n):
            if i in memo:
                return memo[i]
            if i == n:
                return 0
            idx = arr[i][0]
            ni = bisect_left(arr, endTime[idx], key=lambda x:x[1])
            memo[i] = max(profit[idx]+dfs(ni, n), dfs(i+1, n))
            return memo[i]

        memo = dict()
        n = len(startTime)
        # arr = [(idx, stime)]
        arr = sorted(enumerate(startTime), key=lambda x:x[1])

        return dfs(0, n)