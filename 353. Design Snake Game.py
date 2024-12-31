"""
745 ms runtime beats 5.09%
799.11 MB memory beats 5.09%
"""
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        self.m = height
        self.n = width
        # snake_head, not occupy grid
        self.head = [0, 0]

        # record snake_body occupy grid
        self.block = [[False] * self.n for _ in range(self.m)]
        self.snakebody = deque()

        # food index
        self.food = food
        self.fi = 0

    def move(self, direction: str) -> int:
        # pre take tail if body_head follow snake_head
        ti = tj = None
        if self.snakebody and self.block[self.head[0]][self.head[1]] is False:
            ti, tj = self.snakebody.pop()
            self.block[ti][tj] = False

        # check new snake_head condition
        ci, cj = self.head
        di, dj = self.dirs[direction]
        ni, nj = ci + di, cj + dj
        if ni < 0 or ni >= self.m or nj < 0 or nj >= self.n or self.block[ni][nj]:
            return -1

        # move snake_head and body_head
        self.head = [ni, nj]
        if ti is not None:
            self.snakebody.appendleft((ci, cj))
            self.block[ci][cj] = True

        # check food eaten and grow body_head at snake_head
        if self.fi < len(self.food) and self.head == self.food[self.fi]:
            self.snakebody.appendleft((ni, nj))
            self.block[ni][nj] = True
            self.fi += 1
        return len(self.snakebody)
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)