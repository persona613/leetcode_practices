"""
137 ms runtime beats 59.72%
16.94 MB memory beats 85.37%
"""
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        bts = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        ans = 0
        for n, u in bts:
            if n <= truckSize:
                truckSize -= n
                ans += n * u
            else:
                ans += truckSize * u
                break
        return ans