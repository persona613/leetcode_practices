"""
104 ms runtime beats 28.26%
18.47 MB memory beats 17.39%
"""
# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        # assume state p = 0, q = 1, first element's state = p
        state = [0] * n

        # check first 5 elements' state
        roll = [1, 2, 3, 4]
        q1 = reader.query(*roll)
        # each time, move one varian to left
        for i in range(4):
            curr = roll[i]
            # move one varain to left
            roll[i] -= 1
            q2 = reader.query(*roll)
            if q2 == q1:
                state[curr] = state[roll[i]]
            else:
                state[curr] = state[roll[i]] ^ 1
            q1 = q2

        # roll = [0, 1, 2, 3] = q1
        # check other elements
        base_point = roll[3]
        for i in range(5, n):
            roll[3] = i
            q2 = reader.query(*roll)
            if q2 == q1:
                state[i] = state[base_point]
            else:
                state[i] = state[base_point] ^ 1

        # state-p count
        cnt = 0
        for s in state:
            if s == 0:
                cnt += 1

        if cnt < n - cnt:
            for i in range(n):
                if state[i] == 1:
                    return i
        elif cnt == n - cnt:
            return -1
        return 0