"""
49 ms runtime beats 40.50%
16.46 MB memory beats 75.00%
"""
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for de in details:
            age = int(de[11:13])
            if age > 60:
                ans += 1
        return ans