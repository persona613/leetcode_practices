"""
Wrong Answer
27 / 56 testcases passed
Input
nums =
[[14,12,19,16,9],[13,14,15,8,11],[11,13,1]]

Use Testcase
Output
[14,13,12,11,11,14,19,13,15,16,1,8,9]
Expected
[14,13,12,11,14,19,13,15,16,1,8,9,11]
"""
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        d = defaultdict(list)
        for i in range(len(nums)-1, -1, -1):
            m = len(nums[i])
            for j in range(m-1, -1, -1):
                d[i+j].append(nums[i][j])
        for k in list(d.keys())[::-1]:
            res.extend(d[k])
        return res
        
        