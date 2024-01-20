"""
Runtime Error
4 / 69 testcases passed
AttributeError: 'SeatManager' object has no attribute 'fress'. Did you mean: 'frees'?
    self.frees[1], self.frees[0] = self.fress[0], self.fress[1]
"""
class SeatManager:

    def __init__(self, n: int):
        self.mxseat = n
        self.next_seat = 1
        # free_seats
        self.frees = []

    def reserve(self) -> int:
        if self.frees:
            self.frees[0], self.frees[-1] = self.frees[-1], self.frees[0]
            nst = self.frees.pop()
            self.heapify(0, len(self.frees))
            return nst
        else:
            self.next_seat += 1
            return self.next_seat - 1

    def unreserve(self, seatNumber: int) -> None:
        self.frees.append(seatNumber)
        if len(self.frees) == 2:
            if self.frees[1] < self.frees[0]:
                self.frees[1], self.frees[0] = self.fress[0], self.fress[1]
            return
        # curr index
        ci = len(self.frees)-1
        # parent index
        pi = ci // 2
        if ci % 2 == 0:
            pi -= 1
        while ci > 0 and self.frees[ci] < self.frees[pi]:
            self.frees[ci], self.frees[pi] = self.frees[pi], self.fress[ci]
            ci = pi
            pi = ci // 2
            if c1 % 2 == 0:
                pi -= 1

    def heapify(self, i, ln) -> None:
        # minist index
        mi = i
        l = i * 2 + 1
        r = i * 2 + 2
        if l < ln and self.frees[l] < self.free[mi]:
            self.free[l], self.free[mi] = self.free[mi], self.free[l]
            mi = l
        if r < ln and self.frees[r] < self.free[mi]:
            self.free[r], self.free[mi] = self.free[mi], self.free[r]
            mi = r
        if mi != i:
            self.heapify(mi, ln)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)