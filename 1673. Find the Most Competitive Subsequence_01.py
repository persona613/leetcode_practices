"""
Time Limit Exceeded
76 / 88 testcases passed
Use Testcase
nums = 
k =
24140
"""
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:

        def dfs(arr, p):
            if not arr: return []
            stk = deque()
            for i in range(len(arr)):
                a = arr[i]
                while stk and stk[-1][0] > a:
                    stk.pop()
                stk.append((a, i))

            if len(stk) >= p:
                return [stk[i][0] for i in range(p)]
            else:
                a, i = stk.popleft()
                right = dfs(arr[i+1:], p - 1)
                left = dfs(arr[:i], p - 1 - len(right))
                return left + [a] + right

        return dfs(nums, k)