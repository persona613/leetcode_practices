"""
613 ms runtime beats 44.32%
32.35 MB memory beats 74.73%
"""
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        m = len(players)
        n = len(trainers)
        i = m - 1
        j = n - 1
        ans = 0
        while i >= 0 and j >= 0:
            if players[i] <= trainers[j]:
                ans += 1
                i -= 1
                j -= 1
            else:
                i -= 1
        return ans
