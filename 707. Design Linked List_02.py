'''
Runtime: 448 ms, faster than 22.17% of Python3 online submissions 
Memory Usage: 14.8 MB, less than 27.26% of Python3 online submissions
'''
class SiglyListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next
    
class MyLinkedList:
            
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
    
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        node = SiglyListNode(val)
        
        if index > self.size:
            return
        elif index <= 0:
            node.next = curr
            self.head = node
        else:
            for _ in range(index-1):
                curr = curr.next
            node.next = curr.next
            curr.next = node            
        self.size += 1            

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        if index < 0 or index >= self.size:
            return
        elif index == 0:
            self.head = curr.next
        else:
            for _ in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1
        
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)