'''
Wrong Answer
'''
class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.hashmap = [ [None, None] for _ in  range(self.size)]

    def put(self, key: int, value: int) -> None:
        self.hashmap[key][0] = key
        self.hashmap[key][1] = value
            
    def get(self, key: int) -> int:
        if self.hashmap[key][0]:
            return self.hashmap[key][1]
        else:
            return -1

    def remove(self, key: int) -> None:
        if self.hashmap[key][0]:
            self.hashmap[key][0] = None
            self.hashmap[key][1] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)