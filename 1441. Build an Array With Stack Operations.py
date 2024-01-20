"""
31 ms runtime beats 96.57%
16.27 MB memory beats 44.85%
"""
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        k = 1
        for t in target:
            while k < t:
                res.append("Push")
                res.append("Pop")
                k += 1
            res.append("Push")
            k += 1
        return res