"""
1357 ms runtime beats 41.38%
42.58 MB memory beats 51.44%
"""
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        mx, mi = arrays[0][-1], arrays[0][0]
        for arr in arrays[1:]:
            diff = max(abs(mx - arr[0]), abs(arr[-1] - mi))
            ans = max(ans, diff)

            mx = max(mx, arr[-1])
            mi = min(mi, arr[0])
        return ans
        
