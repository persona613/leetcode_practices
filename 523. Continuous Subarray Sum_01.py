"""
Wrong Answer
88 / 99 testcases passed

Editorial
Input
nums =
[23,2,4,6,6]
k =
7

Use Testcase
Output
false
Expected
true
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # prefix sum
        ps = [nums[0] % k]
        for v in nums[1:]:
            ps.append((v % k + ps[-1]) % k)
        
        # {rmainder: pre index}
        dic = dict()
        for i in range(len(ps)):
            r = ps[i]
            if r in dic and i - dic[r] > 1:
                return True
            if r not in dic:
                dic[r] = i
        return False