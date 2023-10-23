"""
71 ms runtime beats 54.65%
16.5 MB memory beats 31.85%
"""
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x: (x.bit_count(), x))
        return arr