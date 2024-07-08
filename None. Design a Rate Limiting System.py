"""
397 ms runtime beats None %
47.1 MB memory beats None %
"""
class RateLimiter:

    def __init__(self, n: int, t: int):
        self.timewindow = t
        self.maxrequest = n
        self.q = deque()
        
    def shouldAllow(self, timestamp: int) -> bool:
        pretime = timestamp - self.timewindow + 1
        while self.q and self.q[0] < pretime:
            self.q.popleft()
            
        if len(self.q) < self.maxrequest:
            self.q.append(timestamp)
            return True
        return False


# Your RateLimiter object will be instantiated and called as such:
# obj = RateLimiter(n, t)
# param_1 = obj.shouldAllow(timestamp)