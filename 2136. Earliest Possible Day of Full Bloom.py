"""
1248 ms runtime beats 69.18%
33.52 MB memory beats 73.59%
"""
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        arr = sorted(zip(growTime, plantTime), reverse = True)
        ans = time = -1
        for g, p in arr:
            time += p
            if time + g + 1 > ans:
                ans = time + g + 1
        return ans