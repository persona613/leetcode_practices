'''
Runtime: 35 ms, faster than 87.01% of Python3 online submissions 
Memory Usage: 13.9 MB, less than 76.17% of Python3 online submissions
'''

class MyQueue:

    def __init__(self):
        self.insk = []
        self.otsk = []

    def push(self, x: int) -> None:
        self.insk.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        
        if not self.otsk:
            while self.insk:
                n = self.insk.pop()
                self.otsk.append(n)
        return self.otsk.pop()            

    def peek(self) -> int:
        if self.empty():
            return None
        
        if not self.otsk:
            while self.insk:
                n = self.insk.pop()
                self.otsk.append(n)
        return self.otsk[-1]

    def empty(self) -> bool:
        if self.insk or self.otsk:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()