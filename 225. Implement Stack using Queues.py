'''
Runtime: 64 ms, faster than 16.23% of Python3 online submissions 
Memory Usage: 14 MB, less than 23.57% of Python3 online submissions
'''

class MyStack:

    def __init__(self):
        self.q0 = deque([])
        self.q1 = deque([])
        self.qmap = {0: self.q0, 1: self.q1}
        self.currq = 0
    def push(self, x: int) -> None:
        self.qmap[self.currq].append(x)

    def pop(self) -> int:
        if not self.empty:
            return None
        
        while len(self.qmap[self.currq]) > 1:
            n = self.qmap[self.currq].popleft()
            self.qmap[(self.currq+1)%2].append(n)
            
        elem = self.qmap[self.currq].popleft()
        self.currq = (self.currq+1)%2
        return elem
    
    def top(self) -> int:
        if not self.empty:
            return None
        
        while len(self.qmap[self.currq]) > 1:
            n = self.qmap[self.currq].popleft()
            self.qmap[(self.currq+1)%2].append(n)
        
        elem = self.qmap[self.currq].popleft()
        self.currq = (self.currq+1)%2
        self.qmap[self.currq].append(elem)
        
        return elem

    def empty(self) -> bool:
        return not self.q0 and not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()