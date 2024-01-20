"""
761 ms runtime beats 99.20%
28.46 MB memory beats 6.39%
"""
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        sm = sum(neededTime)
        mx = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                if neededTime[i] > mx:
                    mx = neededTime[i]
            else:
                sm -= mx
                mx = neededTime[i]
        sm -= mx
        return sm