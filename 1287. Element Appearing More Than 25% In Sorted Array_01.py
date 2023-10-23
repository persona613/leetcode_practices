"""
Wrong Answer
23 / 25 testcases passed
Editorial
Input
arr =
[1,2,3,3]

Use Testcase
Output
1
Expected
3
"""
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cnt = 0
        t = len(arr) / 4
        x = arr[0]
        for a in arr:
            if a != x:
                x = a
                cnt = 0
            cnt += 1
            if cnt >= t:
                return x
        return x