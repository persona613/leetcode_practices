"""
Runtime Error
82 / 717 testcases passed
UnboundLocalError: cannot access local variable 't' where it is not associated with a value
          ^
    nxt = t + 2
Line 26 in maximumValueSum (Solution.py)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ret = Solution().maximumValueSum(param_1, param_2, param_3)
Line 61 in _driver (Solution.py)
    _driver()
Line 72 in <module> (Solution.py)
Last Executed Input
Use Testcase
nums =
[100,78,94,46,99]
k =
6
edges =
[[0,1],[1,2],[1,3],[4,3]]
"""
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        flipcard = 0
        xred = []
        for x in nums:
            xred.append((x ^ k) - x)
            if xred[-1] > 0:
                flipcard += 1

        ans = sum(nums)
        if flipcard == 0:
            return ans

        xred.sort(reverse = True)
        if flipcard == 1:
            flipscore = xred[0] + xred[1]
            if flipscore > 0:
                return ans + flipscore

        # add postive score every pair
        for t in range(0, flipcard - 1, 2):
            ans += xred[t] + xred[t + 1]

        # if flipcard is odd
        nxt = t + 2
        if nxt < n and nxt + 1 < n:
            flipscore = xred[nxt] + xred[nxt + 1]
            if flipscore > 0:
                ans += flipscore
        return ans