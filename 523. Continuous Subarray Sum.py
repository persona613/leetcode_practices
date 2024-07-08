"""
874 ms runtime beats 11.53%
36.68 MB memory beats 10.59%
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # prefix sum
        ps = [nums[0] % k]
        for v in nums[1:]:
            ps.append((v % k + ps[-1]) % k)
        
        # {rmainder: pre index}
        dic = dict()
        dic[0] = -1
        for i in range(len(ps)):
            r = ps[i]
            if r in dic and i - dic[r] > 1:
                return True
            if r not in dic:
                dic[r] = i
        return False