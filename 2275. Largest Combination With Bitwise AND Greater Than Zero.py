"""
597 ms runtime beats 30.00%
26.92 MB memory beats 56.67%
"""
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # each 1-bit position count
        cnt = [0] * 24
        for num in candidates:
            pos = 0
            while num:
                cnt[pos] += num & 1
                num >>= 1
                pos += 1
        return max(cnt)