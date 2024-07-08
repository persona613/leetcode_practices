"""
14.38 ms runtime beats 47.12%
17.62 MB memory beats 22.12%
"""
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # pre_mask + substring(1 or 0) = curr_mask
        # pre_mask = curr_mask - substring(1 or 0)
        # find pre_mask's count = find substring's count
        dic = defaultdict(int)
        curr = ans = 0
        for c in word:
            curr ^= 1 << ord(c) - 97
            bc = curr.bit_count()
            # check curr_mask
            if bc == 0 or bc == 1:
                ans += 1

            # check pre_mask (:= curr_mask - 0)
            ans += dic[curr]
            # check pre_mask (:= curr_mask - 1)
            for i in range(10):
                ans += dic[curr ^ (1 << i)]                
            # register curr_mask
            dic[curr] += 1
        return ans