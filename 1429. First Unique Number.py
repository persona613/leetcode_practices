"""
523 ms runtime beats 91.62%
68.80 MB memory beats 25.90%
"""
class FirstUnique:

    def __init__(self, nums: List[int]):
        # for queue, try dict instead of OrderedDict
        self.q = dict()
        self.is_unique = dict()
        for v in nums:
            self.add(v)

    def showFirstUnique(self) -> int:
        if self.q:
            return next(iter(self.q))
        return -1

    def add(self, value: int) -> None:
        if value not in self.is_unique:
            self.is_unique[value] = True
            self.q[value] = None
        elif self.is_unique[value] == True:
            self.is_unique[value] = False
            self.q.pop(value)
        # case 3: self.is_unique[value] == False: not process


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)