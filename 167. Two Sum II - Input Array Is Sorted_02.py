'''
Status: Time Limit Exceeded
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        i = 0
        while i < l-1:
            j = l-1
            while i < j: 
                if numbers[j] == numbers[j-1] and i < j-1:
                    j -= 1
                    continue
                if numbers[j] == target - numbers[i]:
                    return [i+1, j+1]
                j -= 1
            i += 1