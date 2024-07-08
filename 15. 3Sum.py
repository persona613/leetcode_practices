"""
836 ms runtime beats 34.53%
21.00 MB memory beats 18.73%
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def twosum(start, target):
            pres = set()
            pairs = set()
            for u in nums[start:]:
                v = target - u
                if v in pres:
                    # prevent duplicate
                    if (v, u) not in pairs:
                        pairs.add((u, v))
                pres.add(u)
            return pairs

        def isduplicate(pool, c, u, v):
            arr = [c, u, v]
            for i in range(3):
                a = arr[i]
                b = arr[(i + 1) % 3]    
                c = arr[(i + 2) % 3]
                if (a, b, c) in pool or \
                        (a, c, b) in pool:
                    return True
            return False

        n = len(nums)
        res = set()
        seen = set()
        for i in range(n - 2):
            curr = nums[i]
            if curr in seen:
                continue
            seen.add(curr)
            pairs = twosum(i + 1, 0 - curr)
            if pairs:
                for u, v in pairs:
                    if not isduplicate(res, curr, u, v):
                        res.add((curr, u, v))                
        return res