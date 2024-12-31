"""
78 ms runtime beats 64.72%
20.52 MB memory beats 53.25%
"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.q = nums
        heapify(self.q)

    def add(self, val: int) -> int:
        heappush(self.q, val)
        while len(self.q) > self.k:
            heappop(self.q)
        return self.q[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)