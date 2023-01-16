"""
28 ms runtime beats 92.84%
14 MB memory beats 27.70%
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def merge(ds):
            if len(ds) == 0:
                return []
            if len(ds) == 1:
                return list(maps[int(ds)])
            
            ans = []
            i = len(ds)//2
            left = merge(ds[:i])
            right = merge(ds[i:])
            for l in left:
                for r in right:
                    ans.append(l+r)
            return ans
        
        maps = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        return merge(digits)