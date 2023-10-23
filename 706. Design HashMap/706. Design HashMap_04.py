'''
Wrong Answer
27 / 36 testcases passed
'''
class MyHashMap:

    def __init__(self):
        self.hashmap = [[]]*1024

    def put(self, key: int, value: int) -> None:
        index = key//1024
        arr = self.hashmap[index]
        if not arr:
            arr[:] = [-1]*1024
        arr[key-index*1024] = value

    def get(self, key: int) -> int:
        index = key//1024
        arr = self.hashmap[index]
        if not arr:
            return -1
        return arr[key-index*1024]

    def remove(self, key: int) -> None:
        index = key//1024
        arr = self.hashmap[index]
        if not arr: return
        arr[key-index*1024] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)