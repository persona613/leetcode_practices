"""
58 ms runtime beats 87.71%
19.54 MB memory beats 70.89%
"""
class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.q) < self.size:
            self.sum += val
            self.q.append(val)
            return self.sum / len(self.q)
        else:
            self.sum = self.sum-self.q.popleft()+val
            self.q.append(val)
            return self.sum / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)