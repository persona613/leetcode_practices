"""
Runtime Error
6 / 69 testcases passed
NameError: name 'c1' is not defined. Did you mean: 'ci'?
    if c1 % 2 == 0:
"""
class SeatManager:

    def __init__(self, n: int):
        self.mxseat = n
        self.next_seat = 1
        # free_seats
        self.fs = []

    def reserve(self) -> int:
        if self.fs:
            self.fs[0], self.fs[-1] = self.fs[-1], self.fs[0]
            nst = self.fs.pop()
            self.heapify(0, len(self.fs))
            return nst
        else:
            self.next_seat += 1
            return self.next_seat - 1

    def unreserve(self, seatNumber: int) -> None:
        self.fs.append(seatNumber)
        if len(self.fs) == 2:
            if self.fs[1] < self.fs[0]:
                self.fs[1], self.fs[0] = self.fs[0], self.fs[1]
            return
        # curr index
        ci = len(self.fs)-1
        # parent index
        pi = ci // 2
        if ci % 2 == 0:
            pi -= 1
        while ci > 0 and self.fs[ci] < self.fs[pi]:
            self.fs[ci], self.fs[pi] = self.fs[pi], self.fs[ci]
            ci = pi
            pi = ci // 2
            if c1 % 2 == 0:
                pi -= 1

    def heapify(self, i, ln) -> None:
        # minist index
        mi = i
        l = i * 2 + 1
        r = i * 2 + 2
        if l < ln and self.fs[l] < self.fs[mi]:
            self.fs[l], self.fs[mi] = self.fs[mi], self.fs[l]
            mi = l
        if r < ln and self.fs[r] < self.fs[mi]:
            self.fs[r], self.fs[mi] = self.fs[mi], self.fs[r]
            mi = r
        if mi != i:
            self.heapify(mi, ln)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)