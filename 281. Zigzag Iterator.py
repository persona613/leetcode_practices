"""
47 ms runtime beats 48.40%
16.82 MB memory beats 88.63%
"""
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vs = deque()
        if v1:
            self.vs.append((v1, 0))
        if v2:
            self.vs.append((v2, 0))

    def next(self) -> int:
        arr, idx = self.vs.popleft()
        ans = arr[idx]
    
        # left elements in arr
        if idx + 1 < len(arr):
            self.vs.append((arr, idx + 1))
        return ans

    def hasNext(self) -> bool:
        return len(self.vs) > 0



# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())