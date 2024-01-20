'''
Runtime: 2593 ms, faster than 0% of Python3 online submissions 
Memory Usage: 61.3 MB, less than 57.49% of Python3 online submissions
'''
class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        import random
        n = len(self.set)
        r = random.randint(1, n) # include n
        lst = [x for x in self.set]
        return lst[r-1]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()