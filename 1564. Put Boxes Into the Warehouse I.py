"""
438 ms runtime beats 100%
35.66 MB memory beats 35.71%
"""
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # adj room height according pre rooms
        rooms = []
        min_height = warehouse[0]
        for rh in warehouse:
            if rh < min_height:
                min_height = rh
            rooms.append(min_height)
        
        # compare from smallest
        bxs = sorted(boxes, reverse=True)
        ans = 0
        while bxs and rooms:
            if bxs[-1] <= rooms[-1]:
                ans += 1
                bxs.pop()
            rooms.pop()
        return ans       