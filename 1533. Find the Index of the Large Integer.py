"""
147 ms runtime beats 20.32%
55.30 MB memory beats 84.49%
"""
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        l = 0
        r = n - 1
        while l < r:
            if (r - l + 1) % 2:
                spare = r
                r -= 1
            mid = (l + r) // 2
            ret = reader.compareSub(l, mid, mid + 1, r)
            if ret > 0:
                r = mid
            elif ret < 0:
                l = mid + 1
            else:
                return spare
        return l