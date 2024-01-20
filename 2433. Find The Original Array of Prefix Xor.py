"""
667 ms runtime beats 56.00%
36.46 MB memory beats 31.15%
"""
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        for i in range(1, len(pref)):
            arr.append(pref[i]^pref[i-1])
        return arr