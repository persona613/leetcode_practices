'''
runtime beats 42.33%
memory usage beats 0% !!!!!!
'''
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        newlist = []
        for n in arr:
            if n == 0 :
                newlist.append(n)                
            newlist.append(n)
        l = len(arr)
        arr[:] = newlist[:l]