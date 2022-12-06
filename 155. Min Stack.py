'''
Runtime: 3892 ms, faster than 0% of Python3 online submissions 
Memory Usage: 17.9 MB, less than 65.27% of Python3 online submissions
'''

class MinStack:

    def __init__(self):
        self.lst = []        

    def push(self, val: int) -> None:
        self.lst.append(val)

    def pop(self) -> None:
        self.lst.pop()

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        mini = float(inf)
        size = len(self.lst)
        for i in range(size):
            if self.lst[i] < mini:
                mini = self.lst[i]
        return mini
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()