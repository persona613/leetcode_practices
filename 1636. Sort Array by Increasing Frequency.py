"""
52 ms runtime beats 43.07%
16.49 MB memory beats 76.93%
"""
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        # sorted key = (freq of val, -val for decreasing)
        return sorted(nums, key = lambda x: (dic[x], -x))