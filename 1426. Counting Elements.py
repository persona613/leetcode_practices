"""
53 ms runtime beats 13.50%
16.30 MB memory beats 80.14%
"""
class Solution:
    def countElements(self, arr: List[int]) -> int:
        bag = set(arr)
        ans = 0
        for a in arr:
            if a + 1 in bag:
                ans += 1
        return ans