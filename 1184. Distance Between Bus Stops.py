"""
54 ms runtime beats 69.09%
17.35 MB memory beats 73.12%
"""
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        tm = sum(distance)
        if start <= destination:
            dm = sum(distance[start: destination])
        else:
            dm = sum(distance[destination: start])
        return min(dm, tm-dm)

        # if start <= destination:
        #     sum1 = sum(distance[0:start]) + sum(distance[destination:])
        #     sum2 = sum(distance[start:destination])
        # else:
        #     sum1 = sum(distance[0:destination]) + sum(distance[start:])
        #     sum2 = sum(distance[destination:start])
        # return min(sum1, sum2)