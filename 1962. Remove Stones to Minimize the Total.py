"""
853 ms runtime beats 99.78%
30.92 MB memory beats 77.54%
"""
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        mx = max(piles)
        cnt = [0] * (mx + 1)
        for pile in piles:
            cnt[pile] += 1
            
        op = k
        for pile in range(mx, 1, -1):
            take = min(op, cnt[pile])
            cnt[pile] -= take
            cnt[pile - (pile // 2)] += take
            op -= take
            if not op:
                break
        return sum(pile * cnt[pile] for pile in range(mx + 1))