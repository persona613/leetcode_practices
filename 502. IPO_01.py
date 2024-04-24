"""
Runtime Error
3 / 35 testcases passed
IndexError: index out of range
         ^^^^^^^^^^^^^^^^
    w -= heapq.heappop(q)

Last Executed Input
Use Testcase
k =
1
w =
0
profits =
[1,2,3]
capital =
[1,1,2]
"""
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        arr = sorted(zip(capital, profits))
        n = len(arr)
        take = i = 0
        q = []
        while take < k:
            while i < n and arr[i][0] <= w:
                heapq.heappush(q, -arr[i][1])
                i += 1
            w -= heapq.heappop(q)
            take += 1
        return w