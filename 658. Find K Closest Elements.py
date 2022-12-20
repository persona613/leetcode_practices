"""
828 ms runtime beats 34.91%
15.5 MB memory beats 80.72%
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = deque()
        # index of x
        curr = None
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l+r) // 2
            if arr[m] == x:
                curr = m
                break
            elif arr[m] < x:
                l = m+1
            elif arr[m] > x:
                r = m-1
                
        # not found x
        if curr == None:
            st = r
            nd = l
        else:
            res.append(arr[curr])
            k -= 1
            st = curr-1
            nd = curr+1
            
        for _ in range(k):
            if st < 0:
                res.append(arr[nd])
                nd += 1
            elif nd >= len(arr):
                res.appendleft(arr[st])
                st -= 1
            elif abs(arr[st]-x) <= abs(arr[nd]-x):
                res.appendleft(arr[st])
                st -= 1
            else:
                res.append(arr[nd])
                nd += 1        
        
        return res 
        