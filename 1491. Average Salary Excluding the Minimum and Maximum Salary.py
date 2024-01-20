"""
38 ms runtime beats 62.58%
16.46 MB memory beats 5.95%
"""
class Solution:
    def average(self, salary: List[int]) -> float:
        mi = mx = salary[0]
        t = 0
        for sa in salary:
            t += sa
            if sa < mi:
                mi = sa
            if sa > mx:
                mx = sa
        return (t-mi-mx) / (len(salary)-2)