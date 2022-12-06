'''
Runtime: 160 ms, faster than 30.72% of Python3 online submissions 
Memory Usage: 14.4 MB, less than 86.42% of Python3 online submissions
'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.size = 0
        self.bucket = []
        self.start = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.size == 0:
            self.start = 0
            self.tail = 0
            
            # check list index if out of range
            if len(self.bucket) == 0:
                self.bucket.append(value)
            else:
                self.bucket[self.tail] = value
            self.size += 1
            return True
        
        if (self.tail+1) % self.space == self.start:
            return False
        
        self.tail = (self.tail+1) % self.space
        
        # check list index if out of range
        if self.tail < len(self.bucket):
            self.bucket[self.tail] = value
        else:
            self.bucket.append(value)
            
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        if self.size == 1:
            self.start = None
            self.tail = None
            self.size -= 1
            return True
        
        self.start = (self.start+1) % self.space
        self.size -= 1
        return True
    
    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.bucket[self.start]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.bucket[self.tail]

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False        

    def isFull(self) -> bool:
        if self.size == self.space:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

