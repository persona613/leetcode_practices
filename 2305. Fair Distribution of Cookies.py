"""
6169 ms runtime beats 15.96%
701.68 MB memory beats 5.06%
"""
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        def backtrack(ci, mean):
            if ci == n:
                res.append(max(childrens))
                return
            
            cnt = cookies[ci]
            for p in range(k):
                if childrens[p] < mean:
                    childrens[p] += cnt
                    backtrack(ci + 1, mean)
                    childrens[p] -= cnt

        n = len(cookies)
        mean = sum(cookies) / k
        childrens = [0] * k
        res = []
        backtrack(0, mean)
        return min(res)
