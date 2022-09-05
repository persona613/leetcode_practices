'''
29 / 33 test cases passed.
Status: Time Limit Exceeded
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                a.append(i)
        return a