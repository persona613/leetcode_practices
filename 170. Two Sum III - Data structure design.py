"""
277 ms runtime beats 48.72%
20.79 MB memory beats 91.05%
"""
class TwoSum:

    def __init__(self):
        self.arr = []
        self.found_pair = set()

    def add(self, number: int) -> None:
        self.arr.append(number)

    def find(self, value: int) -> bool:
        if value in self.found_pair:
            return True
        bag = set()
        for a in self.arr:
            if a in bag:
                self.found_pair.add(value)
                return True
            bag.add(value - a)
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)