'''
Status: Time Limit Exceeded
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        for i in range(l):
            for j in range(i+1,l):
                if numbers[j] == target - numbers[i]:
                    return [i+1, j+1]