"""
396 ms runtime beats 71.68%
29.55 MB memory beats 31.15%
"""
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        arr = sorted(skill)
        l = 0
        r = len(arr) - 1
        p = arr[l] + arr[r]
        res = 0
        while l < r:
            if arr[l] + arr[r] != p:
                return -1
            res += arr[l] * arr[r]
            l += 1
            r -= 1
        return res