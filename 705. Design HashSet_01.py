'''
Runtime: 348 ms, faster than 60.95% of Python3 online submissions 
Memory Usage: 18.9 MB, less than 50.92% of Python3 online submissions
'''
class MyHashSet:

    def __init__(self):
        self.hashset = set()

    def add(self, key: int) -> None:
        self.hashset.add(key)

    def remove(self, key: int) -> None:
        self.hashset.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.hashset


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)