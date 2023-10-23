"""
Runtime Error
4 / 87 testcases passed
RuntimeError: dictionary changed size during iteration
    for k in cds.keys():
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cds = dict()
        for x in nums:
            if len(cds) < 2:
                cds[x] = 1
            elif x in cds:
                cds[x] += 1
            else:
                for k in cds.keys():
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

            