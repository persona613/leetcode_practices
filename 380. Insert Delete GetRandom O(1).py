"""
280 ms runtime beats 84.29%
64.26 MB memory beats 39.43%
"""
class RandomizedSet:

    def __init__(self):
        self.dic = dict()
        self.arr = list()

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.dic[val] = len(self.arr)
            self.arr.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dic:
            t = self.dic[val]
            self.arr[t], self.arr[-1] = self.arr[-1], self.arr[t]
            v = self.arr[t]
            self.dic[v] = t

            del self.dic[val]
            self.arr.pop()
            return True
        else:
            False

    def getRandom(self) -> int:
        i = random.randrange(len(self.arr))
        return self.arr[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()