'''
Runtime: 669 ms, faster than 32.39% of Python3 online submissions 
Memory Usage: 17.2 MB, less than 64.78% of Python3 online submissions
'''
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hashmap = [ [] for _ in range(self.size) ]

    def put(self, key: int, value: int) -> None:
        subkey = key % self.size      
        for i in range(len(self.hashmap[subkey])):
            if self.hashmap[subkey][i][0] == key:
                self.hashmap[subkey][i][1] = value
                return
        self.hashmap[subkey].append([key, value])
            
    def get(self, key: int) -> int:
        subkey = key % self.size
        for i in range(len(self.hashmap[subkey])):
            if self.hashmap[subkey][i][0] == key:
                return self.hashmap[subkey][i][1]
        return -1

    def remove(self, key: int) -> None:
        subkey = key % self.size
        for i in range(len(self.hashmap[subkey])):
            if self.hashmap[subkey][i][0] == key:
                del self.hashmap[subkey][i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)