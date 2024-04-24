"""
1179 ms runtime beats 62.04%
39.71 MB memory beats 35.51%
"""
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        def bs(arr, target):
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        potions.sort()
        m = len(potions)
        res = []
        for spell in spells:
            i = bs(potions, success / spell)
            res.append(m - i)
        return res