"""
Wrong Answer
46 / 74 testcases passed
Input
deck =
[1,1,2,2,2,2]

Use Testcase
Output
false
Expected
true
"""
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic = Counter(deck)
        cnts = set(dic.values())
        return 1 not in cnts and len(set(cnts)) == 1