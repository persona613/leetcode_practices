"""
537 ms runtime beats 69.48%
59.22 MB memory beats 70.74%
"""
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dic = dict()
        for v in nums:
            self.dic[v] = self.dic.get(v, 0) + 1
        
        self.q = deque()
        for v in nums:
            if self.dic[v] == 1:
                self.q.append(v)

    def showFirstUnique(self) -> int:
        while self.q and self.dic[self.q[0]] != 1:
            self.q.popleft()
        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        self.dic[value] = self.dic.get(value, 0) + 1
        if self.dic[value] == 1:
            self.q.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)