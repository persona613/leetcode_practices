"""
667 ms runtime beats 10.52%
77.19 MB memory beats 90.17%
"""
class LRUCache:

    def __init__(self, capacity: int):
        self.N = capacity
        self.timecode = 0
        # track min timecode
        self.mintime = 0

        # {key: [timecode, value]}
        self.dict = dict()
        # {timecode: key}, active timecode
        self.keyfinder = dict()

    def get(self, key: int) -> int:
        if key in self.dict:
            self.update_keyfinder(key)
            return self.dict[key][1]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.update_keyfinder(key)
            self.dict[key][1] = value

        elif len(self.dict) < self.N:
            self.timecode += 1
            self.dict[key] = [self.timecode, value]
            self.keyfinder[self.timecode] = key
        else:
            # delete timecode of least recently used
            deltimecode = self.get_mintime()
            delkey = self.keyfinder.pop(deltimecode)
            self.mintime += 1
            del self.dict[delkey]
            self.put(key, value)
    
    def update_keyfinder(self, key):
        # newtimecode
        self.timecode += 1
        oldtimecode = self.dict[key][0]

        # update keyfinder(active timecode)
        self.keyfinder.pop(oldtimecode)
        self.keyfinder[self.timecode] = key
        self.dict[key][0] = self.timecode

    def get_mintime(self):
        while self.mintime not in self.keyfinder:
            self.mintime += 1
        return self.mintime


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)