"""
40 ms runtime beats 61.91%
17.69 MB memory beats 85.89%
"""
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        l = 0
        r = 10 ** 4 - 1
        while l <= r:
            mid = (l + r) // 2
            ret = reader.get(mid)
            if ret == target:
                return mid
            elif ret < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1