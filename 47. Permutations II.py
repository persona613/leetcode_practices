"""
45 ms runtime beats 92.06%
16.84 MB memory beats 52.55%
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(dic, pm):
            if len(pm) == n:
                res.append(pm[:])

            for k in dic.keys():
                if dic[k] > 0:
                    pm.append(k)
                    dic[k] -= 1
                    backtrack(dic, pm)
                    pm.pop()
                    dic[k] += 1
        n = len(nums)
        dic =defaultdict(int)
        for v in nums:
            dic[v] += 1
        res = []
        backtrack(dic, [])
        return res