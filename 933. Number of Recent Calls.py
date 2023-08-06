"""
233 ms runtime beats 97.49%
22.3 MB memory beats 6.55%
"""
class RecentCounter:

    def __init__(self):
        self.acnt = 0 # accumulative
        self.q = deque() #[[t, acnt],...]

    def ping(self, t: int) -> int:
        self.acnt += 1
        self.q.append([t, self.acnt])
        k = t - 3000
        while k > self.q[0][0]:
            self.q.popleft()
        return self.acnt - self.q[0][1] + 1
            

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)