"""
Runtime Error
3 / 52 testcases passed
TypeError: list indices must be integers or slices, not NoneType
       ~~~~~~~~~~~^^^
    if cnt_by_cols[j] == 1:
Line 21 in findLonelyPixel (Solution.py)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ret = Solution().findLonelyPixel(param_1)
Line 42 in _driver (Solution.py)
    _driver()
Line 53 in <module> (Solution.py)
Last Executed Input
Use Testcase
picture =
[["W","W","W"],["W","W","W"],["W","W","W"]]
"""
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])
        cnt_by_cols = [0] * n
        cands = []
        for i in range(m):
            # first "B" index each row
            pos = None
            for j in range(n):
                if picture[i][j] == "B":
                    cnt_by_cols[j] += 1
                    if pos is None:
                        pos = j
                    else:
                        pos = -1
            if j >= 0:
                cands.append(pos)
        ans = 0
        for j in cands:
            if cnt_by_cols[j] == 1:
                ans += 1
        return ans