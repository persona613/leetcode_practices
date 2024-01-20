"""
82 ms runtime beats 55.91%
16.46 MB memory beats 59.48%
"""
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False
        return Counter(target) == Counter(arr)