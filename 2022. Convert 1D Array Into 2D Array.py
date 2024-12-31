"""
653 ms runtime beats 97.65%
23.78 MB memory beats 79.94%
"""
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        res = []
        for i in range(0, len(original), n):
            # print(i)
            res.append(original[i:i+n])        
        return res