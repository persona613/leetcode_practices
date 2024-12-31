"""
61 ms runtime beats 50.13%
17.24 MB memory beats 73.27%
"""
class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [None] * k
        self.size = k
        self.st = 0
        self.nd = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.q[self.st] = value
        else:
            self.st = (self.st - 1) % self.size
            self.q[self.st] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.q[self.nd] = value
        else:
            self.nd = (self.nd + 1) % self.size
            self.q[self.nd] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.st == self.nd:
            self.q[self.st] = None
        else:
            self.st = (self.st + 1) % self.size
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.st == self.nd:
            self.q[self.st] = None
        else:
            self.nd = (self.nd - 1) % self.size
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.st]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.nd]

    def isEmpty(self) -> bool:
        return self.st == self.nd and self.q[self.st] == None

    def isFull(self) -> bool:
        return (self.nd + 1) % self.size == self.st


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()