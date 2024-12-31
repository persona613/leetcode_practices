"""
1562 ms runtime beats 46.83%
51.89 MB memory beats 5.85%
"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # pre row point A = (a,b)
        # if b <= j, get = p(a,b)+p(i,j)-(j-b)
        # if b >= j, get = p(a,b)+p(i,j)+(j-b)
        # left_max = p(a,b)+b, right_max = p(a,b)-b
        # dp[i][j] = p(i,j) + max(left_max-j, right_max+j)
        m = len(points)
        n = len(points[0])
        dp = points[0]
        for i in range(1, m):
            curr = points[i][:]
            # left max
            left = [dp[0] + 0]
            for b in range(1, n):
                left.append(max(left[-1], dp[b] + b))
            # right max
            right = deque([dp[n - 1] - (n - 1)])
            for b in range(n - 2, -1, -1):
                right.appendleft(max(right[0], dp[b] - b))

            for j in range(n):
                curr[j] += max(left[j] - j, right[j] + j)
            dp = curr
        return max(dp)