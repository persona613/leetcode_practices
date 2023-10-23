"""
Wrong Answer
76 / 87 testcases passed
Editorial
Input
nums = [2,2,1,3]

Use Testcase
Output
[]
Expected
[2]
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

            