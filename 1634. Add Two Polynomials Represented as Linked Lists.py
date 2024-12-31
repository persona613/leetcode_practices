"""
301 ms runtime beats 86.87%
26.12 MB memory beats 70.20%
"""
# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        dummy = curr = PolyNode()
        while poly1 and poly2:
            if poly1.power == poly2.power:
                coe = poly1.coefficient + poly2.coefficient
                if coe:
                    curr.next = PolyNode(coe, poly1.power)
                    curr = curr.next
                poly1 = poly1.next
                poly2 = poly2.next

            elif poly1.power > poly2.power:
                curr.next = poly1
                curr = curr.next
                poly1 = poly1.next
            else:
                curr.next = poly2
                curr = curr.next
                poly2 = poly2.next

        if not poly1:
            curr.next = poly2
        elif not poly2:
            curr.next = poly1
        return dummy.next