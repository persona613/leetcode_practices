'''
Runtime: 115 ms, faster than 20.24% of Python3 online submissions
Memory Usage: 14 MB, less than 53.34% of Python3 online submissions
'''
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        a = set()
        for i in range(len(arr)):
            if arr[i]*2 in a:
                return True
            if arr[i] % 2 == 0:
                if arr[i] / 2 in a:
                    return True
            a.add(arr[i])
        return False
                