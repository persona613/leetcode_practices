"""
117 ms runtime beats 87.68%
14.3 MB memory beats 41.54%
"""
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l = 0
        r = n-1
        
        while l <= r:
            m = (l+r)//2
            if letters[m] == target:                
                while m+1 < n:
                    if letters[m+1] != letters[m]:
                        return letters[m+1]
                    m += 1
                return letters[(m+1)%n]
            elif letters[m] > target:
                r = m-1
            elif letters[m] < target:
                l = m+1
        return letters[l%n]