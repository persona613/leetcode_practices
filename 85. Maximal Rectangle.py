"""
215 ms runtime beats 74.85%
18.08 MB memory beats 14.93%
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def cal(arr): # problem 84.
            stk = [-1]
            max_area = 0
            for i in range(n):
                while stk[-1] != -1 and arr[stk[-1]] >= arr[i]:
                    curr_height = arr[stk.pop()]
                    area = curr_height * (i - stk[-1] -1)
                    max_area = max(max_area, area)
                stk.append(i)
            while stk[-1] != -1:
                curr_height = arr[stk.pop()]
                area = curr_height * (n - stk[-1] - 1)
                max_area = max(max_area, area)
            return max_area

        m = len(matrix)
        n = len(matrix[0])
        dp = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    dp[j] = 0
                else:
                    dp[j] += 1
            area = cal(dp)
            ans = max(ans, area)
        return ans