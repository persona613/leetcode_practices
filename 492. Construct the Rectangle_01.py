"""
Wrong Answer
output: [1 ,2]
expect: [2, 1]
"""
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mid = int(area**0.5)
        for i in range(mid, area+1):
            if area % i == 0:
                return [i, int(area/i)]
