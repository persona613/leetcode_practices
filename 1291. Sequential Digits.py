"""
44 ms runtime beats 15.53%
16.55 MB memory beats 63.35%
"""
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ds = "123456789"
        res = []
        for size in range(2, 10):
            for i in range(size, 10):
                num = int(ds[i-size:i])
                if low <= num <= high:
                    res.append(num)
        return res