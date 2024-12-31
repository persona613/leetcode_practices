"""
0 ms runtime beats 100.00%
17.01 MB memory beats 11.56%
"""
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        def both(lst1, lst2):
            res = []
            m = len(lst1)
            n = len(lst2)
            i = j = 0
            while i < m and j < n:
                if lst1[i] == lst2[j]:
                    res.append(lst1[i])
                    i += 1
                    j += 1
                elif lst1[i] < lst2[j]:
                    i += 1
                else:
                    j += 1
            return res

        return both(arr1, both(arr2, arr3))