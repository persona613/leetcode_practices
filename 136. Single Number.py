'''
Runtime: 4568 ms, faster than 8.66% of Python3 online submissions 
Memory Usage: 16.8 MB, less than 18.97% of Python3 online submissions
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = []
        for n in nums:
            if n not in ans:
                ans.append(n)
            else:
                ans.remove(n)
        return ans[0]