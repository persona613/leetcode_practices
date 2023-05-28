"""
1156 ms runtime beats 25.62%
16.2 MB memory beats 12.19%
"""
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mid = int(area**0.5)
        for i in range(mid, area+1):
            if area % i == 0 and i >= area//i:
                return [i, area//i]
