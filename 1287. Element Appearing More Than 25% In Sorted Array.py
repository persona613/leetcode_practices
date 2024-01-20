"""
78 ms runtime beats 97.31%
17.63 MB memory beats 59.65%
"""
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        # occurs times of x > size
        size = n // 4
        for i in range(n-size):
            if arr[i] == arr[i+size]:
                return arr[i]
        return -1
