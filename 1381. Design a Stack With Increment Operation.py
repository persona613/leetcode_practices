"""
67 ms runtime beats 94.21%
17.44 MB memory beats 87.29%
"""
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxsize = maxSize
        self.stk = []
        self.addmap = dict()

    def push(self, x: int) -> None:
        if len(self.stk) < self.maxsize:
            self.stk.append(x)

    def pop(self) -> int:
        if not self.stk:
            return -1
        ln = len(self.stk)
        # dict.pop(key, default_value) -> key's value
        val = self.addmap.pop(ln, 0)
        if ln > 1:
            self.addmap[ln - 1] = self.addmap.get(ln - 1, 0) + val
        return self.stk.pop() + val

    def increment(self, k: int, val: int) -> None:
        r = min(k, len(self.stk))
        self.addmap[r] = self.addmap.get(r, 0) + val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)