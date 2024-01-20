"""
53 ms runtime beats 7.03%
16.38 MB memory beats 10.07%
"""
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                ans += 1
        return ans