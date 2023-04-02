"""
1176 ms runtime beats 5.1%
14.1 MB memory beats 9.35%
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def pick(t):
            if t < 0:
                return
            for num in candidates: 
                combine.append(num)
                if t - num == 0:
                    if not checkexist(combine):
                        res.append(combine[:])
                    combine.pop()
                    return
                else:
                    pick(t - num)
                    combine.pop()
                    
        def checkeq(lst1, lst2):
            for n in set(lst1):
                if lst1.count(n) != lst2.count(n):
                    return False
            return True
        def checkexist(lst):
            for r in res:
                if len(r) != len(lst):
                    continue
                if set(r) != set(lst):
                    continue
                if checkeq(r, lst):
                    return True
            return False
                            
        res = []
        combine = []
        candidates.sort()
        pick(target)
        return res