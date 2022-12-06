"""
Input:
["MyCircularQueue","enQueue","deQueue","enQueue","enQueue","deQueue","isFull","isFull","Front","deQueue","enQueue","Front","enQueue","enQueue","Rear","Rear","deQueue","enQueue","enQueue","Rear","Rear","Front","Rear","Rear","deQueue","enQueue","Rear","deQueue","Rear","Rear","Front","Front","enQueue","enQueue","Front","enQueue","enQueue","enQueue","Front","isEmpty","enQueue","Rear","enQueue","Front","enQueue","enQueue","Front","enQueue","deQueue","deQueue","enQueue","deQueue","Front","enQueue","Rear","isEmpty","Front","enQueue","Front","deQueue","enQueue","enQueue","deQueue","deQueue","Front","Front","deQueue","isEmpty","enQueue","Rear","Front","enQueue","isEmpty","Front","Front","enQueue","enQueue","enQueue","Rear","Front","Front","enQueue","isEmpty","deQueue","enQueue","enQueue","Rear","deQueue","Rear","Front","enQueue","deQueue","Rear","Front","Rear","deQueue","Rear","Rear","enQueue","enQueue","Rear","enQueue"]
[[81],[69],[],[92],[12],[],[],[],[],[],[28],[],[13],[45],[],[],[],[24],[27],[],[],[],[],[],[],[88],[],[],[],[],[],[],[53],[39],[],[28],[66],[17],[],[],[47],[],[87],[],[92],[94],[],[59],[],[],[99],[],[],[84],[],[],[],[52],[],[],[86],[30],[],[],[],[],[],[],[45],[],[],[83],[],[],[],[22],[77],[23],[],[],[],[14],[],[],[90],[57],[],[],[],[],[34],[],[],[],[],[],[],[],[49],[59],[],[71]]
Output:
[null,true,true,true,true,true,false,false,12,true,true,28,true,true,13,13,true,true,true,24,24,12,24,24,true,true,27,true,27,27,45,45,true,true,45,true,true,true,45,false,true,17,true,45,true,true,45,true,true,true,true,true,88,true,99,false,88,true,88,true,true,true,true,true,28,28,true,false,true,30,66,true,false,66,66,true,true,true,77,66,66,true,false,true,true,true,90,true,90,47,true,true,57,87,57,true,57,57,true,true,49,true]
Expected:
[null,true,true,true,true,true,false,false,12,true,true,28,true,true,45,45,true,true,true,27,27,13,27,27,true,true,88,true,88,88,24,24,true,true,24,true,true,true,24,false,true,47,true,24,true,true,24,true,true,true,true,true,53,true,84,false,53,true,53,true,true,true,true,true,66,66,true,false,true,45,17,true,false,17,17,true,true,true,23,17,17,true,false,true,true,true,57,true,57,87,true,true,34,92,34,true,34,34,true,true,59,true]

"""

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
        else:
            self.tail = (self.tail+1) % self.space
            
            # check list index if out of range
            if len(self.bucket) < self.space:
                self.bucket.append(value)
            else:    
                self.bucket[self.tail] = value
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
        else:
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