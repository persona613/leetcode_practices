"""
Submission Result: Time Limit Exceeded 
Last executed input:
10
7
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def record_same(com):
            same = []
            tmp = [None]*k
            def pk(i):
                for p in com:
                    if p not in tmp:
                        tmp[i] = p
                        if i+1 == k:
                            same.append(tmp[:])                  
                        else:
                            pk(i+1)
                        tmp[i] = None
            pk(0)
            key = " ".join([str(i) for i in com])
            seen[key] = same
            
        def checkdiff(com):
            for key in seen.keys():
                if com in seen[key]:
                    return False
            return True

        def pick(i):
            for d in range(1, n+1):
                if d not in com:
                    com[i] = d
                    if i+1 == k:
                        if checkdiff(com):
                            ans.append(com[:])
                            record_same(com)
                    else:
                        pick(i+1)
                    com[i] = None   
 
        seen = {}
        ans = []
        com = [None]*k
        pick(0)
        return ans