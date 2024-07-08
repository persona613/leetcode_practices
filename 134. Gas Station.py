"""
952 ms runtime beats 26.14%
22.00 MB memory beats 33.37%
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        def travel(i):
            tank = gas[i] - cost[i]
            j = i
            for _ in range(n):
                j = (j + 1) % n
                tank += gas[j] - cost[j]
                if tank < 0:
                    break
            return j

        # if from a stuck at b, all points between also stuck
        n = len(gas)
        i = 0
        while i < n:
            if gas[i] - cost[i] >= 0:
                stop = travel(i)
                # print(f"start={i}, stop={stop}")
                if stop == i:
                    return i
                if stop < i:
                    return -1
                i = stop + 1
            else:
                i += 1
        return -1