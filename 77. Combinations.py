"""
335 ms runtime beats 79.15%
16 MB memory beats 18.27%
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def pick(i, f):
            for d in pool[f:]:
                com[i] = d
                if i+1 == k:
                    ans.append(com[:])
                else:
                    pick(i+1, com[i])             

        ans = []
        com = [None]*k
        pool = [i for i in range(1, n+1)]
        pick(0, 0)
        return ans