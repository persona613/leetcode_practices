"""
514 ms runtime beats 8.58%
42.63 MB memory beats 90.62%
"""
class SeatManager:

    def __init__(self, n: int):
        self.mxseat = n
        self.next_seat = 1
        # free_seats
        self.fs = []

    def reserve(self) -> int:
        # print("reserve:", self.fs)
        if self.fs:
            self.fs[0], self.fs[-1] = self.fs[-1], self.fs[0]
            nst = self.fs.pop()
            self.heapify(0, len(self.fs))
            # print("after reserve:", self.fs)
            return nst
        else:
            self.next_seat += 1
            # print("after reserve:", self.fs)
            return self.next_seat - 1

    def unreserve(self, seatNumber: int) -> None:
        # print("unreserve:", self.fs, seatNumber)
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
            if ci % 2 == 0:
                pi -= 1
        # print("after unreserve:", self.fs)

    def heapify(self, i, ln) -> None:
        # minist index
        mi = i
        l = i * 2 + 1
        r = i * 2 + 2
        if l < ln and self.fs[l] < self.fs[mi]:
            mi = l
        if r < ln and self.fs[r] < self.fs[mi]:
            mi = r
        if mi != i:
            self.fs[mi], self.fs[i] = self.fs[i], self.fs[mi]
            self.heapify(mi, ln)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)