"""
533 ms runtime beats 95.20%
22.81 MB memory beats 60.06%
"""
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        friends = sorted(range(n), key = lambda x: times[x][0])
        leavings = []
        curr_empty_chair = 0
        empty_chairs = []
        for i in friends:
            arr, lea = times[i]
            while leavings and leavings[0][0] <= arr:
                _, chair = heappop(leavings)
                heappush(empty_chairs, chair)

            if i == targetFriend:
                break
            if empty_chairs:
                heappush(leavings, (lea, heappop(empty_chairs)))
            else:
                heappush(leavings, (lea, curr_empty_chair))
                curr_empty_chair += 1
        return empty_chairs[0] if empty_chairs else curr_empty_chair