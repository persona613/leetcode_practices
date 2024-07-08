"""
168 ms runtime beats 5.23%
14.5 MB memory beats 32.71%
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # i is index
        def pick(i, k):
            if k == 0:
                maps[k].append(set())
                return
            for p in nums[i:]:
                if p not in tmp:
                    tmp.add(p)
                    if i+1 == k:
                        if tmp not in maps[k]:
                            maps[k].append(tmp.copy())
                    else:
                        pick(i+1, k)
                    tmp.remove(p)   
        res = []     
        tmp = set()
        maps = {k:[] for k in range(len(nums)+1)}
        mid = len(nums) // 2
        for k in range(mid+1):
            pick(0, k)

        nums_set = set(nums)
        for k in range(mid+1, len(nums)+1):
            for st in maps[len(nums)-k]:
                maps[k].append(nums_set - st)
        for lst in maps.values():
            res.extend(lst)
        return res
