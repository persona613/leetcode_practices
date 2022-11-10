'''
Runtime: 157 ms, faster than 97.58% of Python3 online submissions 
Memory Usage: 18.7 MB, less than 67.39% of Python3 online submissions
'''
class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.hashset = [ [] for _ in range(self.size) ]

    def add(self, key: int) -> None:
        subkey = key % self.size
        if not key in self.hashset[subkey]:
            self.hashset[subkey].append(key)

    def remove(self, key: int) -> None:
        subkey = key % self.size
        if key in self.hashset[subkey]:
            self.hashset[subkey].remove(key)

    def contains(self, key: int) -> bool:
        subkey = key % self.size
        return key in self.hashset[subkey]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)