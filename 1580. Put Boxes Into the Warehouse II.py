"""
445 ms runtime beats 91.07%
35.56 MB memory beats 48.21%
"""
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # compare from largest box with both side warehouse
        boxes.sort(reverse=True)
        bn = len(boxes)
        i = l = ans = 0
        r = len(warehouse) - 1
        while i < bn and l <= r:
            if boxes[i] <= warehouse[l]:
                ans += 1
                i += 1
                l += 1
            elif boxes[i] <= warehouse[r]:
                ans += 1
                i += 1
                r -= 1
            else:
                i += 1
        return ans
        