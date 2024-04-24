"""
86 ms runtime beats 84.63%
16.88 MB memory beats 87.05%
"""
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        def bs(arr, target):
            # print(f"start find {target}")
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = (l + r) //2
                # print({f"mid: {mid, arr[mid]}"})
                if arr[mid] <= target:
                    l = mid + 1
                else:
                    r = mid -1
            return l

        nums.sort()        
        arr = []
        sm = 0
        for v in nums:
            sm += v
            arr.append(sm)

        res = []
        for q in queries:
            res.append(bs(arr, q))
        return res