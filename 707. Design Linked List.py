'''
Runtime: 948 ms, faster than 0% of Python3 online submissions 
Memory Usage: 14.9 MB, less than 28.95% of Python3 online submissions
'''
class SiglyListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next
    
class MyLinkedList:
    head: SiglyListNode
        
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head == None:
            if index == 0:
                return -1
            else:
                return -1
        cur = self.head
        i = 0
        while True:
            if index == i:
                return cur.val
            if cur.next == None:
                break
            cur = cur.next
            i += 1
        return -1            

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            self.head = SiglyListNode(val)
        else:
            node = SiglyListNode(val)
            node.next = self.head
            self.head = node

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = SiglyListNode(val)
        else:
            node = SiglyListNode(val)
            cur = self.head
            while True:
                if cur.next == None:
                    break
                cur = cur.next
            cur.next = node            

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head
        node = SiglyListNode(val)
        prev = None
        i = 1
        if index == 0:
            self.addAtHead(val)
            return None
        if self.head == None:
            return None
        while True:
            prev = cur
            cur = cur.next
            if index == i:
                node.next = cur
                prev.next = node                
                break
            if cur.next == None:
                break
            i += 1
        if index == i+1:
            cur.next = node
        else:
            return None

    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return None
        if self.get(index) == -1:
            return None
        if index == 0:
            cur = self.head
            self.head = cur.next
            return None
           
        cur = self.head
        prev = None
        target = None
        i = 1
        while True:
            prev = cur
            cur = cur.next
            if index == i:
                prev.next = cur.next
                return None
            if cur.next == None:
                return None
            i += 1
        
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)