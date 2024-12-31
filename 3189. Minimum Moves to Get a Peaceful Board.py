"""
216 ms runtime beats 47.73%
16.73 MB memory beats 34.66%
"""
class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        # row distribute
        rd = 0
        arr = sorted(rooks, key = lambda x: x[0])
        for i in range(len(arr)):
            rd += abs(i - arr[i][0])
        # col distribute
        cd = 0
        arr = sorted(rooks, key = lambda x: x[1])
        for i in range(len(arr)):
            cd += abs(i - arr[i][1])
        return rd + cd
        