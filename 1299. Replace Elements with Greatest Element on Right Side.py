'''
Runtime: 258 ms, faster than 40.42% of Python3 online submissions
Memory Usage: 15 MB, less than 98.74% of Python3 online submissions
'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return arr
        ln = len(arr)
        i = -1
        maxn = 0
        last = arr[-1]
        while i >= -ln:            
            if i == -1:
                arr[i] = -1
            elif i == -2:
                maxn = max(arr[i], last)
                arr[i] = last                
            else:
                last = arr[i]
                arr[i] = maxn
                maxn = max(maxn, last)
            i -= 1
        return arr
            