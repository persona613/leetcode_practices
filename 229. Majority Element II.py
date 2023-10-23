"""
112 ms runtime beats 51.76%
17.6 MB memory beats 84.36%
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cds = dict()
        for x in nums:
            if x in cds:
                cds[x] += 1
            elif len(cds) < 2:
                cds[x] = 1
            else:
                ks = list(cds.keys())
                for k in ks:
                    if cds[k] > 1:
                        cds[k] -= 1
                    else:
                        del cds[k]
        res = []
        t = len(nums)/3
        for k in cds.keys():
            if nums.count(k) > t:
                res.append(k)
        return res            