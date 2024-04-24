"""
161 ms runtime beats 54.03%
18.16 MB memory beats 21.53%
"""
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        if k == 0:
            return sum(sweetness)
        if k + 1 == len(sweetness):
            return min(sweetness)
            
        def sep(sweet):
            p = 0 # party nums
            st = 0 # accum sweets
            for v in sweetness:
                st += v
                if st >= sweet:
                    p += 1
                    st = 0
            return p            

        l = min(sweetness)
        r = sum(sweetness)
        while l <= r:
            mid = (l + r) // 2
            p = sep(mid)
            if p < k + 1:
                r = mid - 1
            else:
                l = mid + 1
        return r