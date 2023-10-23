"""
32 ms runtime beats 95.89%
16.55 MB memory beats 37.97%
"""
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(1, 1+(n//2)):
            res += [i, -i]
        return res+[0] if n%2 ==1 else res