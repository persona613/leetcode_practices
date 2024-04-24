"""
128 ms runtime beats 88.95%
18.06 MB memory beats 63.51%
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       cnt = Counter(nums)
       return max(cnt.keys(), key=cnt.get)