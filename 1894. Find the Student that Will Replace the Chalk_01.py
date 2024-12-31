"""
Time Limit Exceeded
67 / 72 testcases passed
Last Executed Input
Use Testcase
chalk =
[1]
k =
1000000000
"""
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        remain = k
        sm = sum(chalk)
        while remain >= sm:
            remain -= sm
        for i in range(len(chalk)):
            if remain >= chalk[i]:
                remain -= chalk[i]
            else:
                break
        return i