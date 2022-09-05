'''
Runtime: 118 ms, faster than 19.69% of Python3 online submissions for Shuffle the Array.
Memory Usage: 14.1 MB, less than 90.31% of Python3 online submissions for Shuffle the Array.
'''
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0]*2*n
        r = 0
        for i in range(0, 2*n, 2):
            ans[i] = nums[r]
            ans[i+1] = nums[r+n]
            r += 1
        return ans