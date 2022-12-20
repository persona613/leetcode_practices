'''
Runtime: 463 ms, faster than 0% of Python3 online submissions 
Memory Usage: 14.8 MB, less than 89.11% of Python3 online submissions
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        i = 0

        while i < l-1:
            if numbers[i] == numbers[i+1]:
                if target == numbers[i] + numbers[i+1]:
                    return [i+1, i+2]
                i += 1
                continue
            j = l-1
            while i < j: 
                if numbers[j] == numbers[j-1] and i<j-1:
                    j -= 1
                    continue
                if numbers[j] == target - numbers[i]:
                    return [i+1, j+1]
                j -= 1
            i += 1