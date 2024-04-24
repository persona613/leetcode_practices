"""
98 ms runtime beats 53.04%
17.38 MB memory beats 24.77%
"""
class SmallestInfiniteSet:

    def __init__(self):
        self.q = [i for i in range(1, 1001)]
        heapq.heapify(self.q)
        self.book = [True] * 1001

    def popSmallest(self) -> int:
        val = heapq.heappop(self.q)
        self.book[val] = False
        return val

    def addBack(self, num: int) -> None:
        if self.book[num] == False:
            self.book[num] = True
            heapq.heappush(self.q, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)