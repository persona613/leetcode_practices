"""
67 ms runtime beats 46.88%
21.68 MB memory beats 58.67%
"""
class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.M = len(vec)
        self.counts = []
        for i in range(self.M):
            self.counts.append(len(vec[i]))
        print(self.counts)
        self.vec = vec
        # x=row, y=colume
        self.x = 0
        self.y = 0
        # update x, y to true element
        self.hasNext()

    def next(self) -> int:
        ans = self.vec[self.x][self.y]
        self.y += 1
        self.hasNext()
        return ans

    def hasNext(self) -> bool:
        if self.x < 0 or self.y < 0:
            return False

        while self.x < self.M and self.y >= self.counts[self.x]:
            self.x += 1
            self.y = 0

        if self.x >= self.M:
            self.x = -1
            self.y = -1
            return False
        return True



# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()