"""
581 ms runtime beats 68.47%
31.14 MB memory beats 15.29%
"""
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        t = 0
        for a in nums:
            t ^= a
        return int.bit_count(t ^ k)