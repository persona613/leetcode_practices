"""
Time Limit Exceeded
5 / 48 testcases passed

Use Testcase
temperatures =
[34,80,80,34,34,80,80,80,80,34]
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0] * len(temperatures)
        mx = 0
        for i in range(len(temperatures)-1, -1, -1):
            if temperatures[i] > mx:
                mx = temperatures[i]
                continue
            day = 1
            while temperatures[i + day] <= temperatures[i]:
                day += arr[i + day]
            arr[i] = day
        return arr

            