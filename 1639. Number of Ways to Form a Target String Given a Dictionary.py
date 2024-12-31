"""
2115 ms runtime beats 16.08%
54.57 MB memory beats 37.53%
"""
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        # (word index i, target index ti)
        @lru_cache(None)
        def dp(i, ti, ln, tn):
            if ti == tn:
                return 1
            # if len(freq) - i < len(target) - ti:
                # return 0

            counts = 0
            char_idx = ord(target[ti]) - ord("a")
            for k in range(i, ln - (tn - ti) + 1):
                if freq[k][char_idx] > 0:
                    counts += dp(k + 1, ti + 1, ln, tn) * freq[k][char_idx] % MOD
            return counts % MOD

        # chars frequency
        ln = len(words[0])
        freq = [[0] * 26 for _ in range(ln)]
        for word in words:
            for i in range(ln):
                freq[i][ord(word[i]) - ord("a")] += 1

        MOD = 10 ** 9 + 7
        return dp(0, 0, ln, len(target))