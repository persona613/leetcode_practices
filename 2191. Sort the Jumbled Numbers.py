"""
883 ms runtime beats 86.96%
24.77 MB memory beats 53.80%
"""
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def change(val, rule):
            new_val = []
            for c in str(val):
                new_val.append(rule[c])
            return int("".join(new_val))

        # string mapping
        mapp = dict()
        for i, d in enumerate(mapping):
            mapp[str(i)] = str(d)
        
        # map new int
        new = []
        for v in nums:
            new.append(change(v, mapp))
        
        n = len(nums)
        arr = sorted(range(n), key = lambda i: (new[i], i))
        res = []
        for i in arr:
            res.append(nums[i])
        return res