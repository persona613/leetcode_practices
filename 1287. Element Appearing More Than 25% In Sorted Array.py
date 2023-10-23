"""
76 ms runtime beats 98.75%
17.6 MB memory beats 72.48%
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
            if cnt > t:
                return x
        return x