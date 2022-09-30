'''
Runtime: 76 ms, faster than 18.98% of Python3 online submissions 
Memory Usage: 14.9 MB, less than 82.90% of Python3 online submissions
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        rdict = {}        
        curr = head
        dummyhead = Node(0)
        dummy = dummyhead
        
        while curr:
            
            newnode = Node(curr.val)
            rdict[curr] = newnode
            dummy.next = newnode
            dummy = dummy.next
            curr = curr.next
            
        # print(old[0].random)
        curr = head
        dummy = dummyhead.next
        while dummy:
            dummy.random = rdict.get(curr.random)
            dummy = dummy.next
            curr = curr.next
        return dummyhead.next
        
        