'''
Runtime: 218 ms, faster than 91.39% of Python3 online submissions 
Memory Usage: 15.5 MB, less than 0% of Python3 online submissions 
'''
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        j = i + 1
        left = False
        right = False
        if len(arr) < 3:
            return False
        
        # 左側坡         
        while j < len(arr) and right==False:
            if arr[i] < arr[j]:
                left = True
                i += 1
                j += 1
            elif arr[i] == arr[j]:
                return False
            else:
                right = True
                
        # judge mountain
        else:
            if left == True and right == True:
                pass
            else:
                return False
        # 右側坡
        while j < len(arr):
            if arr[i] > arr[j]:
                i += 1
                j += 1
            else:
                return False
        return True
                
            
        