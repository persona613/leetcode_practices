"""
330 ms runtime beats 92.02%
44.24 MB memory beats 82.89%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        peaks = []
        curr = head
        i = 0
        up = down = False
        while curr.next:
            if curr.val < curr.next.val:
                up = True
            elif curr.val > curr.next.val:
                down = True
            else:
                up = down = False

            # local maximum / minimum
            if up and down:
                peaks.append(i)
                # prepare detect for next segment
                if curr.val < curr.next.val:
                    down = False
                else:
                    up = False
            curr = curr.next
            i += 1
        
        if len(peaks) < 2:
            return [-1, -1]
        mi = i
        for j in range(1, len(peaks)):
            if peaks[j] - peaks[j - 1] < mi:
                mi = peaks[j] - peaks[j - 1]
        return [mi, peaks[-1] - peaks[0]]