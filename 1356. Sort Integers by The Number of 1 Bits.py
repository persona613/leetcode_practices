"""
65 ms runtime beats 74.71%
16.25 MB memory beats 94.41%
"""
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (x.bit_count(), x))