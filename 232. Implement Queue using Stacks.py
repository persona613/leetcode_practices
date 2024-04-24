'''
Runtime: 39 ms, faster than 41.34% of Python3 online submissions 
Memory Usage: 16.62 MB, less than 59.46% of Python3 online submissions
'''
class MyQueue:

    def __init__(self):
        self.instk = []
        self.otstk = []

    def push(self, x: int) -> None:
        self.instk.append(x)

    def pop(self) -> int:
        if not self.otstk:
            while self.instk:
                self.otstk.append(self.instk.pop())
        return self.otstk.pop()     

    def peek(self) -> int:
        if self.otstk:
            return self.otstk[-1]
        else:
            return self.instk[0]

    def empty(self) -> bool:
        return not self.instk and not self.otstk


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()