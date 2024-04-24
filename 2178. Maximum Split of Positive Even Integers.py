"""
286 ms runtime beats 57.14%
29.16 MB memory beats 64.58%
"""
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        res = []
        k = 2
        while finalSum:
            if finalSum < 2 * k + 2: # next 2 even number
                res.append(finalSum)
                break
            res.append(k)
            finalSum -= k
            k += 2
        return res