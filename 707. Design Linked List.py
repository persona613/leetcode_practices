'''
Runtime: 439 ms, faster than 23.77% of Python3 online submissions 
Memory Usage: 15.5 MB, less than 13.51% of Python3 online submissions
'''
class DoublyListNode:
    def __init__(self, val: int, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    
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
        node = DoublyListNode(val)
        
        if index > self.size:
            return
        elif index <= 0:
            node.next = curr
            if curr:
                curr.prev = node
            self.head = node
        else:
            for _ in range(index-1):
                curr = curr.next
            node.next = curr.next
            node.prev = curr
            if curr.next:
                curr.next.prev = node
            curr.next = node            
        self.size += 1            

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        if index < 0 or index >= self.size:
            return
        elif index == 0:
            self.head = curr.next
            if curr.next:
                curr.next.prev = None
        else:
            for _ in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
            if curr.next:
                curr.next.prev = curr
        self.size -= 1
        
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)